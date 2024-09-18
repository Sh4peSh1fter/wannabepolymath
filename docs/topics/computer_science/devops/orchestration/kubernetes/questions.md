---
tags:
  - "interview questions"
  - "kubernetes questions"
---

# **Kubernetes** Questions

## General

1.  What is **Kubernetes**?

    **Kubernetes** is an open-source container orchestration platform that automates the **Deployment**, scaling, and management of containerized applications.

2.  What is the difference between **Docker** and **Kubernetes**?

    - And between **Docker Swarm**?

    **Docker** is a platform for building, running, and managing containers, while **Kubernetes** is a container orchestration platform that manages containerized applications across a cluster of machines.

    **Docker Swarm** is **Docker**'s native clustering and orchestration tool. It is easier to set up but lacks the extensive features of **Kubernetes**, such as autoscaling, robust networking, and persistent storage management.

---

## Basic Components / Architecture

1.  What are the node types / roles?

    there are two types of nodes:

    Master node - Manages the **Kubernetes** cluster, runs control plane components like the API server, scheduler, **etcd**, and controller managers.  
    Worker node - Runs the containerized applications and manages pods via the Kubelet and **kube-proxy**.

2.  What processes run on the master node?

    - And on the worker node?

      The main processes on the master node are:

      **kube-apiserver** - Front-end to the **Kubernetes** control plane.  
      **etcd** - Key-value store that stores cluster data.  
      **kube-scheduler** - Assigns pods to nodes.  
      **controller manager** - Runs controller processes.

      The main processes on the worker node are:

      **kubelet** - Agent that communicates with the master node.  
      **kube-proxy** - Manages network rules.  
      **Container runtime** - Runs the containers (e.g., **Docker**, **containerd**).

3.  What is **etcd** in **Kubernetes**?

    - How does **etcd** ensure consistency in a **Kubernetes** cluster?

      **etcd** is a distributed key-value store that stores all cluster data.  
      It uses the Raft consensus algorithm to ensure consistent replication of data across all **etcd** instances.

4.  How do you back up and restore **etcd**?

    Use `etcdctl snapshot save` to back up and `etcdctl snapshot restore` to restore data.

5.  What are best practices for maintaining **etcd**?

    Run **etcd** on dedicated instances.  
     Enable snapshots.  
     Ensure the quorum (odd number of members).

6.  What is a **controller manager**?

    - What types of controller managers are there?
    - Can you create a new one or configure an existing one?

      A **Controller Manager** in **Kubernetes** is a daemon that manages the control loops that regulate the state of the cluster. Controllers continuously monitor the current state of cluster resources and compare them with the desired state. If a deviation is found, they take corrective actions to bring the actual state back to the desired one.

      Types of Controller Managers:  
      Node Controller - Monitors the health of nodes and performs actions like evicting pods from unhealthy nodes.  
      Replication Controller - Ensures the specified number of pod replicas are running at any given time.  
      Endpoint Controller - Manages the association between services and pods.  
      Service Account Controller - Handles the creation of default accounts and tokens for pods.  
      Job Controller - Ensures jobs are completed successfully.

      you can create or configure a new controller through Custom Controllers. For example, you can develop your own controller using the **Kubernetes** controller-runtime libraries to manage custom resources (CRDs).

7.  What is **kube-proxy**?

    - Can I change and reconfigure it?

      **kube-proxy** is a network proxy that runs on each node in the **Kubernetes** cluster. It maintains network rules on nodes, which allow for communication between pods, and between pods and services, by managing IP tables or IPVS rules.  
      It manages network traffic routing for services by forwarding requests to the appropriate backend pods, and implements service discovery and load balancing by ensuring that the correct backend pods receive requests sent to a service's ClusterIP.

      You can reconfigure **kube-proxy** by modifying its configuration file or using the `--config` flag at startup. For example, you can switch the mode between iptables and ipvs based on your performance or traffic requirements.

---

### Namespaces

1.  What is a namespace?

    - What are they used for?

      A namespace is a logical partition within a **Kubernetes** cluster, providing isolation for resources.  
      They are used for organizing, separating, and managing resources for different environments, teams, or projects.

2.  Can resources from one namespace access resources on another namespace?

    - How to restrict resource usage for namespace?

      By default, resources in one namespace cannot access resources in another unless explicitly allowed. Network policies and Role-Based Access Control (RBAC) can be used to enforce this restriction.

      To restrict resource usage, you can use:  
      Resource Quotas - Limit the number of resources (e.g., CPU, memory, storage) that a namespace can use.  
      LimitRanges - Define minimum and maximum resource limits (e.g., CPU, memory) that pods or containers in the namespace can request or consume.

      For example, if you want to restrict a development namespace to only 4 CPUs and 8GB of memory, you can create a ResourceQuota like this:

      ```yaml
      apiVersion: v1
      kind: ResourceQuota
      metadata:
      name: dev-quota
      namespace: development
      spec:
      hard:
        cpu: "4"
        memory: 8Gi
      ```

### Pods

1.  What is a pod?

    A pod is the smallest deployable unit in **Kubernetes** that contains one or more containers.

2.  How the containers in the pod are managed?

    - why would you contain multiple containers in a pod?

      Containers in a pod share the same network namespace and storage volumes. They are managed together as a single entity.  
      Containers that need to share resources or closely communicate should be placed in the same pod, such as a web server and a logging sidecar.

3.  How does pod scheduling work?

    Pod scheduling refers to the process of assigning a pod to a node. The **Kubernetes** scheduler is responsible for this. It considers a variety of factors to make scheduling decisions, including:  
     Resource requests and limits - Does the node have enough CPU and memory?  
     Node labels - Pods with certain affinities or tolerations might require specific node characteristics.  
     Pod affinity/anti-affinity - Pods can be scheduled near or away from other pods.  
     Node taints and tolerations - Nodes may be tainted to prevent specific pods from being scheduled unless they can tolerate the taint.

4.  What happens when a pod is deleted?

    The containers in the pod are terminated, and the pod object is removed from the cluster.

5.  How can you restrict certain pods from running on specific nodes in **Kubernetes**?

    You can restrict pods from running on certain nodes using:  
     Node taints and pod tolerations - You can taint a node so that only pods with a specific toleration can run on it. For example, if a node is tainted with `dedicated=production:NoSchedule`, only pods with a toleration for this taint will be scheduled on this node.  
     Node selectors - You can specify a node label that a pod must match to be scheduled on that node. for example, Using a node selector like this ensures that a pod only runs on nodes with the label `disktype=ssd`.  
     Node Affinity - A more expressive way to control where pods are scheduled using `requiredDuringSchedulingIgnoredDuringExecution` or `preferredDuringSchedulingIgnoredDuringExecution` rules.

6.  What is a side car in **Kubernetes**?

    A sidecar is a container that runs alongside the main container in a pod to enhance its functionality. It’s often used for tasks like logging, monitoring, proxying, or updating the main application.

---

### Workloads / Sets

#### Deployments

1.  What is a **Deployment**?

    A **Deployment** is a controller that manages the desired state of pod replicas, allowing for updates and scaling.

2.  How do you perform a rolling update?

    By updating the **Deployment**, **Kubernetes** automatically performs a rolling update of pods with minimal downtime.

3.  How do you rollback a **Deployment**?

    Use `kubectl rollout undo Deployment <Deployment-name>` to revert to a previous version.

4.  How do you scale a **Deployment**?

    Use `kubectl scale Deployment <Deployment-name> --replicas=<number>` to adjust the number of pod replicas.

5.  What **Deployment** strategies does a **Deployment** support and how to change it?

    **Kubernetes** **Deployment**s support several strategies for rolling out updates:  
     Rolling Update (default) - Updates pods incrementally, minimizing downtime.
    **Recreate** - Terminates all existing pods before creating new ones.

    You can change the **Deployment** strategy in the spec of a **Deployment** YAML:

    ```yaml
    spec:
    strategy:
      type: RollingUpdate # or Recreate
    ```

    You can further configure the rolling update strategy with parameters like `maxSurge` and `maxUnavailable` to control how many pods are created or deleted during the update.

---

#### ReplicaSets

1.  What is a **ReplicaSet**?

    - How is it different from a **Deployment**?

      A **ReplicaSet** ensures that a specified number of pod replicas are running at all times.

---

#### StatefulSets

1.  What is a **StatefulSet**?

    - When would you use it?

      **StatefulSets** manage stateful applications by maintaining stable network identities and persistent storage.  
      Use a **StatefulSet** for applications that require stable, persistent storage or ordered **Deployment** and scaling (e.g., databases).

2.  What are the use cases for the persistent storage in **StatefulSets**?

    Persistent storage ensures that data remains available even if the pod is rescheduled to a different node.

---

#### DaemonSets

1.  What is a **DaemonSet**?

    - When would you use it?

      A **DaemonSet** ensures that a copy of a pod runs on all (or selected) nodes in the cluster.  
      **DaemonSet**s are useful for deploying system-level services like log collectors or monitoring agents on every node.

2.  How does a **DaemonSet** ensure that a pod is running on every node?

    The **DaemonSet** controller schedules a pod on each node as it joins the cluster.

3.  How do you update a **DaemonSet**?

    Update the **DaemonSet** specification, and **Kubernetes** will update each pod in turn.

4.  How can you run a **DaemonSet** on only subset of nodes?

    You can use nodeSelector or node affinity to limit which nodes run the **DaemonSet** pods.

---

1.  What is the difference between a **Deployment**, a **ReplicaSet**, a **StatefulSet** and a **DaemonSet**?

    **Deployment** - Manages stateless applications and scaling.  
     **ReplicaSet** - Ensures a specified number of pod replicas.  
     **StatefulSet** - Manages stateful applications with persistent data and ordered **Deployment**.  
     **DaemonSet** - Ensures that a pod runs on all or selected nodes.

---

### ConfigMaps and Secrets

1.  What is a **ConfigMap**?

    - When would you use it?

      A **ConfigMap** is an API object used to store non-confidential data in key-value pairs.  
      Use a **ConfigMap** to store configuration data that is consumed by containers.

2.  What is a Secret in **Kubernetes**?

    A Secret stores sensitive data like passwords, tokens, and keys.

3.  What is the difference between a **ConfigMap**s and secrets?

    **ConfigMap**s store plain text data, while Secrets are designed to hold sensitive information and are base64-encoded.

4.  How do you mount a secret ot a **ConfigMap** in a pod?

    You can mount a **ConfigMap** or Secret as an environment variable or volume in the pod.  
     Example of mounting a **ConfigMap** as a volume:

    ```yaml
    volumes:
    - name: config-volume
       **ConfigMap**:
          name: my-config-map
    containers:
    - name: my-container
       volumeMounts:
          - name: config-volume
          mountPath: "/etc/config"
    ```

5.  Can **ConfigMaps** and Secrets be updated and used without restarting pods?

    Yes, **ConfigMaps** and Secrets can be updated. However, for pods to pick up the changes, certain conditions must be met:  
     Mounted as volumes - When mounted as files in a pod, the updates are automatically reflected, but the application needs to monitor for changes.  
     Environment variables: If **ConfigMap**s or Secrets are set as environment variables, the pod needs to be restarted to pick up the changes.

---

### Custom Resource Definitions (CRDs)

1.  What is a Custom Resource Definition (CRD) in **Kubernetes**?

    - When should you use it?
    - How do you create and manage CRDs?

      CRDs are extensions of the **Kubernetes** API that allow you to define your own resource types.  
      Use CRDs to manage applications that require additional types not provided by **Kubernetes** out of the box.  
      CRDs can be defined in YAML files and managed with `kubectl apply` and `kubectl delete`.

      For example, if you're building a database operator, you can create a Database CRD that allows users to create and manage databases as if they were **Kubernetes** resources.

2.  Can you extend existing **Kubernetes** API resources using CRDs?

---

## Networking

#### Services

1.  What is a service?

    A Service is an abstraction that defines a logical set of pods and a policy for accessing them.

2.  What types of services are there?

    - What are the differences between them?

      **ClusterIP** - Default service type, exposes the service only within the cluster.  
      **NodePort** - Exposes the service on each node's IP at a static port.  
      **LoadBalancer** - Exposes the service externally using a cloud provider's load balancer.

3.  How does a service discover the IP of a pod?

    In **Kubernetes**, services are used to expose a set of pods as a single network endpoint. When a pod is created, it is assigned an IP address. The service discovers the IPs of the pods it should route traffic to through **label selector**s and **endpoint**s.

    The **label selector** in the service definition identifies which pods the service is associated with.
    The **Endpoint Controller** ensures that the service knows the IP addresses of the pods selected by the **label selector**.

    When a pod is created, the IP is registered with the service as an endpoint. **Kubernetes** uses a DNS system, usually via **CoreDNS**, which creates DNS records for services, allowing other pods to resolve a service name to the appropriate pod IP.

    For example, a service named my-service can be resolved as `my-service.default.svc.cluster.local` within the cluster.

4.  How do you expose a service externally?

    Use a `NodePort` or `LoadBalancer` service to expose an application outside the cluster.

---

#### Ingress

1.  What is an ingress in **Kubernetes**?

    An Ingress is an API object that manages external access to services, typically via HTTP/HTTPS.

2.  What is the difference between an Ingress and a Service?

    A Service exposes a set of pods under a single IP and port, providing a stable endpoint for accessing this group of pods, while an Ingress provides external access to those services via defined routing rules. It allows for URL-based routing, load balancing, SSL termination, and more. Ingress is often backed by an Ingress Controller like NGINX or Traefik.

3.  How do you set up ingress rules?

    Ingress rules define how external traffic is routed to services inside the cluster. You can set up rules for host-based or path-based routing.  
     here is an example of a simple ingress rule for routing HTTP traffic:

    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
    name: example-ingress
    spec:
    rules:
       - host: "example.com"
          http:
          paths:
             - path: /api
                pathType: Prefix
                backend:
                service:
                   name: api-service
                   port:
                      number: 80
             - path: /web
                pathType: Prefix
                backend:
                service:
                   name: web-service
                   port:
                      number: 80
    ```

4.  What is an ingress controller?

    An Ingress Controller is a specialized load balancer for managing Ingress resources. It watches the **Kubernetes** API for changes in Ingress resources and updates the underlying routing configuration based on these resources.

    Each Ingress Controller has its own set of features for handling load balancing, SSL termination, and URL/path-based routing.

---

#### CNI

1.  What is a CNI?

    - how does it work?

      CNI is the specification and plugins used by **Kubernetes** to manage pod networking.

2.  What is the default CNI?

    **Kubernetes** uses **kube-router**, **Calico**, or **Flannel** by default, depending on the setup.

3.  What is the difference between types of CNI?

    Different CNI plugins provide different features. For example, **Flannel** focuses on simple overlays, while **Calico** offers advanced network policies and routing.

---

1.  How does networking work in **Kubernetes**?

    **Kubernetes** assigns each pod a unique IP address, and Services or Ingress rules are used to manage traffic to and from pods.

2.  How do pods in **Kubernetes** know which container they should route traffic to when multiple containers are running within a pod?

    In a multi-container pod, containers typically communicate through localhost because they share the same network namespace. **Kubernetes** doesn't automatically route traffic between containers in a pod — instead, you need to explicitly define how containers interact.

3.  What is the difference between **kube-proxy** and **CoreDNS**?

    **kube-proxy** manages traffic routing to services. It operates at the network layer and handles load balancing between pod IPs for services using either iptables or IPVS.  
     **CoreDNS** is responsible for DNS resolution inside the cluster. When a service is created, **CoreDNS** assigns it a DNS name, which can be used by other pods to resolve the service’s IP. **CoreDNS** translates service names like my-service.default.svc.cluster.local into IP addresses.

    **kube-proxy** handles low-level routing and forwarding of traffic to the appropriate pod, while **CoreDNS** is responsible for resolving service names to IPs.

4.  What are network policies?

    A **NetworkPolicy** is a specification that defines what traffic is allowed to flow between pods and other network endpoints (e.g., other pods, services, or external services).

    For example, here is a **NetworkPolicy** that allows ingress traffic on port 80 to the web pod only from pods labeled frontend.

    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
    name: allow-web
    namespace: default
    spec:
    podSelector:
       matchLabels:
          app: web
    ingress:
       - from:
          - podSelector:
                matchLabels:
                role: frontend
          ports:
          - protocol: TCP
             port: 80
    ```

---

## Storage

1.  What is a volume?

    A volume is a directory accessible to containers in a pod, abstracting storage from the lifecycle of a pod.

2.  What is the difference between ephemeral and persistent storage?

    Ephemeral storage is temporary and tied to the lifecycle of a pod.  
     Persistent storage survives even after the pod is deleted, using PersistentVolumes (PVs).

3.  What is a PersistentVolumeClaim (PVC)?

    A PVC is a request for storage by a pod, specifying the amount and access mode for a PersistentVolume.

4.  What are storage classes in **Kubernetes**?

    Storage classes define the types of storage (e.g., SSD, HDD) available to dynamically provision PersistentVolumes.

---

## Security

1.  How does **Kubernetes** handle security at the pod and cluster levels?

    At the pod level:  
     Network Policies - Define which pods can communicate with each other.  
     **SecurityContext** - Controls security settings for pods, such as setting user/group IDs and file permissions.  
     **PodSecurityPolicies** (PSP) - Deprecated but used to control pod security settings like privilege escalation and the use of host networking.

    At the cluster level:  
     RBAC (Role-Based Access Control) - Controls who can access and modify **Kubernetes** resources.  
     TLS Encryption - **Kubernetes** uses certificates to secure communication between its components (e.g., **kubelet**, API server).  
     **etcd** Encryption - Sensitive data in **etcd** can be encrypted to protect cluster secrets.

2.  How do you implement role-based access control (RBAC) in **Kubernetes**?

    RBAC allows you to define roles and role bindings to control what resources and actions are available to users and service accounts.

    First, create a **Role** (within a namespace) or **ClusterRole** (across namespaces) that defines a set of permissions.  
     then bind the role to users or service accounts using a RoleBinding or ClusterRoleBinding.

    For example, this role allows users to read pods in the default namespace:

    ```yaml
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
    namespace: default
    name: pod-reader
    rules:
    - apiGroups: [""]
       resources: ["pods"]
       verbs: ["get", "list"]
    ```

3.  What is a **PodSecurityPolicy**?

    A **PodSecurityPolicy** (PSP) was a cluster-wide resource that controlled security-sensitive aspects of pod specification, such as whether a pod can run as the root user or use host networking. It has been deprecated in **Kubernetes** 1.21 and removed in 1.25, being replaced by other mechanisms like Pod Security Admission.

    PSPs were used to enforce restrictions on pod creation based on security policies.

4.  How do you encrypt Secrets at rest in **Kubernetes**?

    You can configure **Kubernetes** to use encryption providers (like KMS) to encrypt Secrets before storing them in **etcd**.

5.  What are cluster roles in **Kubernetes**?

    A **ClusterRole** in **Kubernetes** defines a set of permissions (rules) that apply across the entire cluster, not just within a single namespace. **ClusterRole**s are typically used for cluster-wide resources like nodes, namespaces, and persistent volumes, but they can also be used to grant permissions for namespaced resources across all namespaces.

    In this example, the **ClusterRole** grants all permissions (verbs: ["*"]) for all API groups and resources:

    ```yaml
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
    name: cluster-admin-role
    rules:
    - apiGroups: ["*"]
       resources: ["*"]
       verbs: ["*"]
    ```

    To assign a **ClusterRole** to a user or service account, a **ClusterRoleBinding** is required.

6.  What is service account in **Kubernetes**?

    A ServiceAccount is an account used by processes running in pods to authenticate to the **Kubernetes** API and interact with cluster resources. Each pod has access to a service account, and it is used to associate running processes with certain permissions or policies.

    For example, by default, every pod runs under a service account named default in the respective namespace. You can create custom service accounts for specific tasks:

    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
    name: custom-sa
    namespace: my-namespace
    ```

    The service account token is automatically mounted into the pod as a secret and can be used by the application to make requests to the API server.

    You can specify a custom service account in a pod definition:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: my-pod
    spec:
    serviceAccountName: custom-sa
    containers:
       - name: my-container
          image: my-image
    ```

---

## Scaling

1.  What is horizontal pod autoscaling in **Kubernetes**?

    Horizontal Pod Autoscaling automatically adjusts the number of pod replicas based on resource utilization.

2.  What is vertical pod autoscaling in **Kubernetes**?

    Vertical Pod Autoscaling adjusts the CPU and memory limits for a pod without increasing the number of replicas.

3.  What is the difference between horizontal pod scaling and vertical pod scaling?

    Horizontal scaling - Adds more pod replicas.  
     Vertical scaling - Increases the resource limits for a single pod.

4.  How does **Cluster Autoscaler** work?

    The **Cluster Autoscaler** adjusts the number of nodes in a cluster based on pod resource requests and utilization.

5.  What is KEDA in **Kubernetes**?

    - How does it work?

      **KEDA** (**Kubernetes** Event-Driven Autoscaling) is an open-source project that allows **Kubernetes** to scale applications based on events from external sources (e.g., message queues, databases, HTTP traffic) in addition to traditional CPU/Memory-based autoscaling. **KEDA** enables event-driven autoscaling by integrating with **Kubernetes** Horizontal Pod Autoscalers (HPA).

      It supports various event sources like Azure Service Bus, Kafka, AWS SQS, RabbitMQ, Prometheus metrics, and more.

      For example, **KEDA** can scale the number of consumers based on the number of messages in the queue:

      ```yaml
      apiVersion: keda.sh/v1alpha1
      kind: ScaledObject
      metadata:
      name: queue-worker
      spec:
      scaleTargetRef:
         name: my-app
      triggers:
         - type: azure-queue
            metadata:
            queueName: myqueue
            queueLength: "5"
      ```

      This configuration scales the my-app **Deployment** based on the length of the Azure queue.

6.  What is **Karpenter** in **Kubernetes**?

    - how does it work?

      **Karpenter** is an open-source cluster autoscaler for **Kubernetes** that automatically provisions new nodes based on the demands of pending pods. Unlike the default **Kubernetes** Cluster Autoscaler, **Karpenter** is more flexible, capable of scaling nodes with diverse requirements such as instance types, zones, and resource capacities.

---

## Monitoring

1.  How do you monitor a **Kubernetes** cluster?

    Use monitoring tools like Prometheus, Grafana, and the **Kubernetes** Dashboard to visualize metrics and health of the cluster.

2.  How can you collect and view logs in **Kubernetes**?

    Logs can be collected with `kubectl logs` for individual pods, or you can set up a centralized logging system like ELK (Elasticsearch, Logstash, Kibana).

---

## Upgrades and Maintenance

1.  How do you upgrade a **Kubernetes** cluster?

    Upgrading a **Kubernetes** cluster involves updating the control plane components (like the API server, controller manager, and scheduler) and the worker nodes to a newer version of **Kubernetes**.

    Steps:  
     Backup **etcd** - Since **etcd** stores all cluster data, creating a backup ensures you can restore the cluster in case something goes wrong.  
     Update the Control Plane - Upgrade the master nodes and control plane components. For managed **Kubernetes** services like GKE or EKS, this is often a one-click process.  
     Update Node Components - Upgrade kubelet and **kube-proxy** on each node, starting with master nodes and then moving to worker nodes.  
     Drain Nodes - When upgrading worker nodes, drain each node before upgrading to ensure workloads are rescheduled on other nodes.  
     Upgrade Node Operating System - If necessary, upgrade the OS packages to ensure compatibility with the new **Kubernetes** version.  
     Test - Verify that workloads are functioning properly after the upgrade.

    For managed **Kubernetes** services (e.g., GKE, EKS), upgrades are typically handled via the cloud provider's platform, making the process simpler.

2.  How do you handle node maintenance in **Kubernetes**?

    Use `kubectl drain` to gracefully evict pods from a node before performing maintenance.

3.  What are disruptive updates, and how do you prevent them?

    A disruptive update is an update that can potentially cause downtime or negatively impact running workloads. Examples include updates to core components like the control plane, node operating systems, or updates that require restarting pods.

    To prevent disruptive updates:  
     Use PodDisruptionBudgets (PDBs) - Ensure that a certain number of pods remain running during an update.  
     Rolling Updates - Apply rolling updates to **Deployment**s to ensure minimal downtime. **Kubernetes** performs rolling updates by gradually replacing old pods with new ones.  
     Draining nodes - Use the kubectl drain command to gracefully evict pods from a node before performing disruptive changes.  
     Monitoring and Alerts - Set up monitoring (e.g., Prometheus) to ensure that you're notified about any potential issues during updates.

4.  How do you handle version compatibility between **Kubernetes** components?

    Always ensure that **Kubernetes** components (API server, **kubelet**, **kube-proxy**, etc.) are compatible with each other by referring to the **Kubernetes** version skew policy.

---

## Disaster Recovery

1.  How do you handle disaster recovery in **Kubernetes**?

    Disaster recovery involves backing up **etcd**, persistent data, and cluster configuration, and restoring it when necessary.

2.  What are **Kubernetes** backups, and how do you perform them?

    **Kubernetes** backups typically involve backing up:  
     Cluster state - The **etcd** database stores all cluster state (configurations, secrets, service accounts, **Deployment**s, etc.). Regular **etcd** backups are critical for disaster recovery.  
     Persistent data - Persistent volumes (e.g., for databases) hold important data for applications and must also be backed up.

    How to perform backups:  
     **etcd** backup - Backing up **etcd** directly is crucial to restore the cluster state in case of a failure. You can use **etcd**’s built-in snapshot feature.

    ```bash
    **etcd**CTL_API=3 **etcd**ctl --endpoints=$ENDPOINTS snapshot save /path/to/backup.db
    ```

    Velero - A popular open-source tool for backing up and restoring **Kubernetes** resources (YAMLs) and persistent volumes. It integrates with cloud storage like AWS S3 or Azure Blob Storage.

    ```bash
    velero backup create my-backup --include-namespaces my-namespace
    ```

    Manual YAML backups Periodically export resource definitions (**Deployment**s, services, secrets, etc.) to YAML files and store them in version control.

3.  How do you recover from a failed **etcd** cluster?

    Restore **etcd** from a snapshot and rejoin the nodes to the cluster.

---

## Operators

1.  What is a **Kubernetes** Operator?

    - when would you use it?

      An Operator is a method of packaging, deploying, and managing a **Kubernetes** application using custom resources.  
      Operators are useful for managing complex applications that need operational tasks automated, such as backups or scaling.

2.  How are Operators different from Helm charts?

    Helm charts are used to deploy applications, while Operators manage the lifecycle and automate complex tasks for those applications.

3.  How do you create a custom operator for an application?

    Use the Operator SDK to develop and deploy a custom operator that extends **Kubernetes** capabilities.

---

## Jobs and CronJobs

1.  What is a job in **Kubernetes**?

    A Job creates one or more pods that run until the specified task is completed.

2.  What is a cronjob in **Kubernetes**?

    - how do you schedule one?

      A CronJob runs Jobs on a scheduled basis, similar to a cron job in Linux. You schedule it using the `schedule` field in the CronJob YAML.

3.  What is the difference between jobs and cronjobs?

    A Job runs once until completion, while a CronJob runs Jobs at regular intervals.

4.  How do you handle failures in Jobs and CronJobs?

    You can configure retries for Jobs, and for CronJobs, you can set `successfulJobsHistoryLimit` and `failedJobsHistoryLimit` to manage job history.

---

## **Deployment** Methods

1.

---

## CLI

1.  What is **kubectl**?
