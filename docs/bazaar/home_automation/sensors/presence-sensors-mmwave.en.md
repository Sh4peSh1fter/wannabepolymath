---
title: "Presence Sensors (mmWave)"
description: "Researching and comparing mmWave radar sensors to find the most reliable options for true presence detection in a smart home."
tags:
  - item
  - item-category:home_automation
  - research
  - comparison
  - corner:bazaar
  - type:blogpost
  - sensor
  - motion-sensor
  - presence-detection
  - mmwave
---

# Presence Sensors (mmWave)

True presence detection is a cornerstone of advanced home automation. Unlike traditional PIR sensors that only detect motion, millimeter-wave (mmWave) radar sensors can detect a person's presence even when they are completely still. This capability is a game-changer for lighting, climate, and other automations, preventing them from turning off when a room is still occupied. My goal is to find reliable and accurate mmWave sensors that integrate seamlessly with Home Assistant for a truly "smart" and responsive home.

---

## Phase 1: Researching the Field

### Keywords, Terms and Concepts

1.  **Sensor Technology**
    *   **Millimeter Wave (mmWave) Radar:** Works by emitting low-power radio waves and analyzing their reflections. It can detect micro-motions like breathing and heartbeats, allowing it to "see" a person in a room regardless of their activity level.
    *   **Presence vs. Occupancy:** A critical distinction. A PIR sensor detects **occupancy** (someone is moving). A mmWave sensor detects true **presence** (someone is in the space, moving or not).
    *   **Fall Detection:** An advanced feature of some mmWave sensors that can detect the sudden change in posture associated with a fall.
2.  **Key Concepts & Features**
    *   **Detection Zones:** The ability to partition a room into multiple zones within the sensor's app or Home Assistant. This allows for highly granular control, such as turning on only the desk lamp when you're at your desk.
    *   **Latency:** The delay between a person entering a zone and the sensor reporting it. While generally low, this can vary between models and firmware versions.
    *   **Sensitivity / Filtering:** The ability to tune the sensor's sensitivity to avoid false positives from things like ceiling fans, curtains moving, or small pets.
    *   **Connectivity:** While some mmWave sensors are Wi-Fi based, Zigbee or Bluetooth models are often preferred for direct integration with Home Assistant to keep traffic off the main Wi-Fi network.

### Guiding Questions

1.  **Are mmWave sensors a complete replacement for PIR sensors?**
    For presence-based automations in primary rooms, yes. However, for simple, battery-powered motion detection in transient spaces (like a closet or pantry), a cheap and efficient PIR sensor can still be a practical choice.
2.  **What are the power requirements?**
    Due to the constant processing required, most high-performance mmWave sensors are wired and require a constant USB power source. Battery-powered mmWave sensors exist but often have compromises in performance or features to conserve energy.
3.  **How complex is the setup?**
    Setup can be more involved than with a simple PIR sensor. It often requires initial configuration of zones and sensitivity tuning to match the specific room layout and achieve maximum reliability.

---

## Phase 2: Defining My Needs & Priorities

1.  **Primary Use Case(s):**
    *   Reliably detect presence in the living room and bedroom to keep lights on when the room is occupied, even if there is no motion.
    *   Instantly trigger lighting automations upon entering a room.
2.  **Key Features Needed:**
    1.  **Performance:**
        *   High accuracy and reliable presence detection.
        *   Low latency for entry/exit events.
        *   Minimal false positives.
    2.  **Configuration:**
        *   Ability to define detection zones.
        *   Adjustable sensitivity.
    3.  **Connectivity:**
        *   Seamless and local integration with Home Assistant.
3.  **Nice to Have:**
    *   Fall detection capabilities.
    *   An integrated lux sensor to prevent lights from turning on when the room is already bright.
4.  **Deal-breakers:**
    *   Inability to detect stationary presence accurately.
    *   Frequent false positives that cannot be tuned out.
    *   Reliance on the cloud for core functionality.

---

## Phase 3: Comparing & Choosing the Item *Type*

With our focus exclusively on mmWave technology for true presence detection, the primary comparison point shifts from the technology itself (PIR vs. mmWave) to the product's form factor and ecosystem. The "types" become different brands and models that implement this technology. Therefore, we will proceed directly to Phase 4.

---

## Phase 4: Choosing the Specific *Product*

The mmWave market is evolving, but three distinct approaches have emerged as top contenders for Home Assistant users.

### Product Options

#### 1. Aqara FP2 Presence Sensor

1.  **Pros:**
    *   **Polished Experience:** A consumer-friendly product with a well-designed mobile app for initial setup.
    *   **Advanced Features:** Excellent zone management (up to 30 zones), multi-person detection, and fall detection.
    *   **Good Integration:** Has a robust official integration for Home Assistant that exposes zone presence and other sensors locally.
2.  **Cons:**
    *   **Wi-Fi Connectivity:** Connects via Wi-Fi, which some advanced users prefer to avoid for IoT devices.
    *   **Cloud for Setup:** Requires the Aqara app and an internet connection for initial setup and firmware updates, though it operates locally with Home Assistant afterward.
    *   **Price:** It is one of the more expensive consumer-grade presence sensors.
3. **Community Opinion:** Widely regarded as the best "out-of-the-box" solution for multi-zone presence detection. Praised for its accuracy and powerful features, with the Wi-Fi dependency being the main drawback for purists.
4. **Price:** High (typically $70-$85).

#### 2. Tuya-based Zigbee Presence Sensors (e.g., ZY-M100)

1.  **Pros:**
    *   **Zigbee Connectivity:** Connects via Zigbee, which is ideal for keeping sensor traffic off the main Wi-Fi network and potentially lower power consumption.
    *   **Affordable:** Often significantly cheaper than the Aqara FP2.
2.  **Cons:**
    *   **Inconsistent Performance:** Quality and features can be a lottery. Some models work well, while others are plagued by false positives or negatives.
    *   **Limited Features:** Most models offer only basic presence detection with no zone management. Configuration options (sensitivity, timeout) can be limited or difficult to access.
    *   **Complex Setup:** Often requires specific configurations or quirks within Zigbee2MQTT to work correctly.
3. **Community Opinion:** A mixed bag. Seen as a budget-friendly option for tinkerers willing to risk getting a "bad" device. Not recommended for critical automations or users who want a "it just works" experience.
4. **Price:** Low to Mid-Range (typically $25-$45).

#### 3. DIY ESPHome Presence Sensor

1.  **Pros:**
    *   **Ultimate Customization:** You have complete control over the hardware and software. You can choose the exact mmWave module, combine it with other sensors (light, temperature), and fine-tune the behavior precisely.
    *   **100% Local:** No cloud or proprietary apps are ever involved.
    *   **Cost-Effective:** Can be the cheapest option if you are comfortable sourcing and assembling the parts.
2.  **Cons:**
    *   **High Technical Barrier:** Requires knowledge of soldering, basic electronics, and YAML configuration for ESPHome.
    *   **Time-Consuming:** Requires significant time for research, assembly, and configuration compared to an off-the-shelf product.
3. **Community Opinion:** The gold standard for power users and DIY enthusiasts. Praised for its unparalleled flexibility and performance when configured correctly. It's the "pro" choice for those who want the absolute best performance and are willing to put in the work.
4. **Price:** Low (typically $15-$30 for parts).

### Comparison Table of Products

| Product         | Ease of Setup      | Features (Zones)  | Connectivity | Overall Match |
|-----------------|:------------------:|:-----------------:|:------------:|:-------------:|
| **Aqara FP2**   | :white_check_mark: | :white_check_mark:| :x: (Wi-Fi)  | 2 / 3         |
| **Tuya Zigbee** | :x:                | :x:               |:white_check_mark:| 1 / 3         |
| **DIY ESPHome** | :x:                | :white_check_mark:|:white_check_mark:| 2 / 3         |

### Conclusion on Specific Product

My choice is the **Aqara FP2 Presence Sensor**.

**Reasoning:** While a DIY solution is powerful, the Aqara FP2 provides the most critical features—especially multi-zone detection—in a reliable, easy-to-use package. For achieving advanced, room-aware automations without the complexity of building a device from scratch, it offers the best balance of power and convenience. The Wi-Fi dependency is a minor, acceptable trade-off for the polished experience and advanced feature set.

---

## Phase 5: Post-Purchase Guide

### 1. Initial Setup (Aqara App)

*   You must first set up the FP2 in the official Aqara Home app. This is required to connect it to your Wi-Fi network and update its firmware.
*   During this process, you will define the room layout and create your detection zones (e.g., "Desk Area," "Couch," "Doorway").

### 2. Home Assistant Integration

*   Once set up, add the Aqara integration in Home Assistant. It will automatically discover the FP2 on your network.
*   The integration will create binary sensor entities for each zone you defined, as well as sensors for presence, light level, and fall detection. These entities will all update locally.

### 3. Best Practices for Placement

*   **Mounting:** For best results, mount the FP2 in a corner of the room, high up on the wall, pointing down towards the center. This gives it the best vantage point to see the entire space.
*   **Avoid Obstructions:** Ensure its view isn't blocked by large furniture.
*   **Minimize False Positives:** Point the sensor away from sources of constant micro-motion, such as ceiling fans, curtains near an air vent, or robotic vacuum docks. You can also use the app to mark these areas as "interference zones" to be ignored.

---

## Phase 6: Essential Accessories & Add-Ons

### 1. Power Supply

*   **Requirement:** The Aqara FP2 is powered by USB-C. It requires a standard 5V/1A USB power adapter.
*   **Recommendation:** Use a reliable power adapter from a reputable brand like Anker or Apple to ensure stable performance.

### 2. USB Cable

*   **Included:** The FP2 comes with a USB-A to USB-C cable.
*   **Extension:** If the included cable isn't long enough to reach your desired mounting location, you will need a longer USB-C cable. Ensure it is a good quality cable rated for power delivery.

---

## Sources & Further Reading

### YouTube Videos

1.  **Smart Home Solver - "The Presence Sensor that Changes Everything"**
    *   *Note:* An excellent, in-depth review of the Aqara FP2's features, setup, and performance in Home Assistant.
2.  **Everything Smart Home - "The Best Presence Sensor for Home Assistant?"**
    *   *Note:* Compares the FP2 to various other Tuya and DIY mmWave sensors, highlighting the pros and cons of each approach.

<https://www.reddit.com/r/homeassistant/comments/1dgeshm/which_mmwave_sensor_should_i_buy/>
<https://www.reddit.com/r/homeassistant/comments/1e8hq48/whats_your_favourite_mmwave_sensor/>
