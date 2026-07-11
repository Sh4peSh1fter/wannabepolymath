---
title: Desk Helping Hand System
description: A design for a desk-mounted helping-hand system for holding tools and parts.
tags:
  - topic:furniture
  - type:how-to
  - status:published
---

# Desk Helping Hand System

## 1. Overview

This document outlines the design and construction of a modular "helping hand" system to be mounted on a desk. The goal is to create a versatile and customizable tool for various tasks such as soldering, crafting, and holding small objects.

## 2. Goals

-   **Modularity:** Easily swap out different "heads" or end-effectors for different tasks.
-   **Customizability:** Leverage 3D printing to create custom parts and attachments.
-   **Stability:** Ensure the system is stable and can securely hold objects.
-   **Reach and Flexibility:** The arms should have a good range of motion.
-   **Aesthetics:** The system should have a clean and organized look.

## 3. Design Considerations

### 3.1. Mounting System: Hybrid Approach

We will implement a hybrid system:

-   **Left Side:** A railway system for a highly flexible arm. This is ideal for tasks requiring frequent repositioning.
-   **Right Side:** A static mounted system for a very stable arm. This is suited for holding heavier objects or for tasks where rigidity is key.

This approach combines the flexibility of a railway with the stability of a fixed mount, offering a versatile solution.

### 3.2. Arm Design

The arms connect the mounting system to the end-effectors.

-   **Material:**
    -   **3D Printed:** PLA, PETG, or ABS for strength. Can be designed for specific needs (e.g., channels for wires).
    -   **Flexible Metal Arms (Gooseneck):** Can be purchased and adapted. Offers good flexibility but can be less rigid.
    -   **Articulated Arms:** Using segments and joints (like Loc-Line or similar 3D printed versions) for maximum posability.

### 3.3. End-Effectors (Heads)

The "business end" of the helping hand. These should be designed to be easily swappable.

-   **Soldering:**
    -   Alligator clips for holding PCBs and wires.
    -   Silicone covers for clips to prevent damage.
-   **Magnification & Lighting:**
    -   A mount for a magnifying glass.
    -   An integrated LED ring light.
-   **Device Holding:**
    -   A clamp or holder for a smartphone or small tablet.
-   **General Purpose:**
    -   Padded clamps for delicate objects.
    -   Small trays for holding components like screws.
-   **Specialized Tools:**
    -   Fume extractor fan mount.
    -   Holder for a small camera (e.g., for recording work).

## 4. Materials and Components

This is a preliminary list of potential materials.

-   **3D Printer Filament:** PETG is a good candidate for its strength and ease of printing.
-   **Fasteners:** An assortment of M3, M4, M5 screws, nuts, and bolts.
-   **Aluminum Extrusions:** If going with the railway system.
-   **Gooseneck Arms:** If not printing articulated arms.
-   **Alligator Clips, Magnifying Glass, LED lights:** To be integrated into the heads.

## 5. Next Steps

-   [ ] Decide on the mounting system (Railway vs. Static).
-   [ ] Sketch initial designs for the chosen system.
-   [ ] Model a prototype of one arm and a simple head (e.g., alligator clip) in CAD software.
-   [ ] 3D print and test the prototype.
-   [ ] Refine the design based on testing.

## 6. Design Sketches

Below are text-based sketches to conceptualize the layout.

### 6.1. Overall Desk Layout

Updated sketch based on the provided photo. The railway will be on the back-left, and the static mount on the front-right.

```
      +------------------------------------------------------+
      |                                                      |
      |                      MONITOR                         |
      |                                                      |
      +------------------------------------------------------+
      
      <-- 3D Printed Railway -->
+--------------------------------------------------------------------+
|                                                                    |
| Clamp-[.._.._.._.._.._.._.._.._.._.._.._.._.._.._..]-Clamp           |
|       |                                                            |
|      / \                                                           | Static
|     /   \                                                          | Mount
|    Arm                                                            o-o-o
|                                                                    |
+--------------------------------------------------------------------+
                        (Front of Desk)
```

### 6.2. Railway System Detail

-   **Rail:** A fully 3D-printed rail system. This will likely be a modular design, with interlocking segments that can be printed and assembled to the desired length. We'll need to design this for rigidity to prevent sagging.
-   **Clamps:** 3D printed, robust clamps to secure the rail segments to the back-left of the desk.
-   **Slider:** A 3D printed piece designed to slide smoothly along the custom printed rail.
-   **Arm Mount:** The helping arm will attach to this slider.

### 6.3. Static Mount Detail

-   **Base:** A heavy-duty, 3D printed clamp attached to the front-right edge of the desk.
-   **Arm Mount:** The base will have a socket or threaded insert to securely hold the arm. Could be a ball joint for some flexibility at the base.


## 7. Inspiration & Sources

A collection of projects and videos that can provide inspiration and technical solutions for our design.

1.  **Mech Arm Railway System:** [https://www.printables.com/model/1027107-mech-arm-railway-system](https://www.printables.com/model/1027107-mech-arm-railway-system) - *A comprehensive railway system that could be a great reference for our flexible side.*
2.  **Multitool Third Arm:** [https://www.printables.com/model/840147-multitool-third-arm](https://www.printables.com/model/840147-multitool-third-arm) - *Features a modular head system.*
3.  **Multifunction Arm Mounting System:** [https://www.printables.com/model/165239-multifunction-arm-mounting-system](https://www.printables.com/model/165239-multifunction-arm-mounting-system) - *Good example of a static, multi-arm base.*
4.  **Flexible & Sturdy Phone Arm (100% Printed):** [https://www.printables.com/model/647794-flexible-sturdy-phone-arm-100-printed](https://www.printables.com/model/647794-flexible-sturdy-phone-arm-100-printed) - *Interesting design for a fully 3D printed, flexible arm.*
5.  **DIY Helping Hands for Electronics:** [https://youtu.be/gMAh_ZKRNnQ?si=vTbE2JESTNDXHsCN](https://youtu.be/gMAh_ZKRNnQ?si=vTbE2JESTNDXHsCN) - *Video with practical tips and ideas.*
6.  **Mechanical Arm Holder System:** [https://makerworld.com/en/models/1183365-mechanical-arm-holder-system#profileId-1194002](https://makerworld.com/en/models/1183365-mechanical-arm-holder-system#profileId-1194002) - *Another modular system with good design elements.*

<https://youtu.be/p0CqYqixMZY?si=XBAvPA2v546uwQ1->
<https://youtu.be/p0CqYqixMZY?si=GBJsdt9wf_fq_v19>
