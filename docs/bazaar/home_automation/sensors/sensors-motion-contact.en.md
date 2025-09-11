---
title: "Sensors (Motion & Contact)"
description: "Researching and comparing motion and contact sensors to find the most reliable, fast, and battery-efficient options for triggering home automations."
tags:
  - item
  - item-category:home_automation
  - research
  - comparison
  - corner:bazaar
  - type:blogpost
  - sensor
  - motion-sensor
  - contact-sensor
  - zigbee
  - presence-detection
---

# Sensors (Motion & Contact)

Sensors are the eyes and ears of a smart home, turning it from a static, remote-controlled system into one that is truly automated and responsive. Motion sensors allow us to trigger actions based on movement, while contact sensors tell us the state of doors, windows, and cabinets. My goal is to find sensors that are fast, reliable, and have excellent battery life, providing the instantaneous feedback needed for seamless automations like turning on lights the moment someone enters a room.

---

## Phase 1: Researching the Field

### Keywords, Terms and Concepts

1.  **Motion Sensor Technology**
    *   **Passive Infrared (PIR) Sensor:** The most common and affordable type. It detects motion by sensing the infrared energy (body heat) of a person moving across its field of view. They are very power-efficient but only detect *motion*, not static presence.
    *   **Millimeter Wave (mmWave) Radar Sensor:** A more advanced technology. It works by emitting radio waves and detecting the subtle changes in their reflections caused by movement—even something as small as breathing. This allows it to detect *presence*, meaning it knows someone is in a room even if they are sitting still.
    *   **Occupancy vs. Presence:** A key distinction. A PIR sensor detects **occupancy** (someone is moving around). A mmWave sensor detects **presence** (someone is in the space, moving or not). This is crucial for lighting automations where you don't want the lights to turn off just because you sat down to read a book.
2.  **Contact Sensor Technology**
    *   **Magnetic Reed Switch:** The universal standard for contact sensors. It consists of two parts: a magnet and a switch. When the magnet is next to the switch (door closed), the circuit is closed. When the magnet moves away (door open), the circuit opens, and the sensor sends a signal.
3.  **Key Concepts & Features**
    *   **Latency:** The delay between the sensor detecting an event and it reporting that event to the hub. For lighting automations, low latency is critical for a responsive feel. Zigbee is excellent for this.
    *   **Timeout / Cooldown Period:** The amount of time a PIR sensor waits after detecting motion before it can report "no motion." A short, configurable timeout is a highly desirable feature.
    *   **Battery Life:** As these are typically small, battery-powered devices, long battery life (1-2+ years) is essential to minimize maintenance.
    *   **Protocol:** **Zigbee** is the ideal protocol for these small, battery-powered devices. It's extremely power-efficient and offers the low latency needed for instant automations.

### Guiding Questions

1.  **PIR or mmWave: Which do I need for lighting?**
    For simple, transient spaces like hallways or closets, a PIR sensor is perfect and cost-effective. For rooms where people will be still for long periods, like a living room or office, a mmWave sensor is far superior as it prevents the lights from turning off unintentionally.
2.  **Why do some motion sensors seem slow?**
    Latency can be caused by the sensor itself, the communication protocol, or the hub's processing speed. Using a high-quality Zigbee sensor with a powerful local hub like Home Assistant results in near-instantaneous response.
3.  **What else can contact sensors be used for?**
    Beyond doors and windows for security, they can be placed on cabinets to turn on interior lights, on refrigerators to send an alert if left open, or even on a pet's food container to log feeding times.

---

## Phase 2: Defining My Needs & Priorities

1.  **Primary Use Case(s):**
    *   Trigger lighting automations instantly upon entering a room (living room, bedroom, hallway).
    *   Turn lights off after a room has been vacant for a set period.
2.  **Key Features Needed:**
    1.  **Performance:**
        *   Extremely low latency for motion triggers.
        *   High reliability and resistance to false positives.
        *   Long battery life (minimum 1 year).
    2.  **Motion Sensor Specifics:**
        *   Configurable timeout/cooldown period.
        *   A mix of PIR for transient spaces and mmWave for presence detection in primary rooms.
    3.  **Connectivity:**
        *   Must use the Zigbee protocol for speed and power efficiency.
        *   Must integrate perfectly with Home Assistant (ZHA or Zigbee2MQTT).
3.  **Nice to Have:**
    *   Small, unobtrusive physical design.
    *   Additional integrated sensors (e.g., light level/lux sensor).
4.  **Deal-breakers:**
    *   Noticeable delay between motion and light activation.
    *   Poor battery life.
    *   Cloud-dependent operation.

---

## Phase 3: Comparing & Choosing the Item *Type*

The main comparison for sensors is the underlying motion detection technology.

### Available Motion Sensor Types

#### 1. Passive Infrared (PIR) Sensors

1.  **Pros:**
    *   Very low cost.
    *   Extremely power efficient, leading to multi-year battery life.
    *   Mature and reliable technology for detecting general motion.
2.  **Cons:**
    *   Cannot detect stationary presence. Will report "no motion" for a person sitting still.
    *   Can be prone to false triggers from non-human heat sources (e.g., heating vents), though good models mitigate this.

#### 2. Millimeter Wave (mmWave) Sensors

1.  **Pros:**
    *   **True Presence Detection:** Can detect a person even when they are completely still. This is a game-changer for lighting automation.
    *   Not affected by heat sources.
    *   Can often define specific detection zones within a room.
2.  **Cons:**
    *   Significantly more expensive than PIR sensors.
    *   Consumes more power, often requiring a wired (USB) power source instead of a battery.
    *   The technology is newer in the consumer space, so product selection is more limited.

### Comparison Table of Sensor Types

| Type          | Presence Detection | Battery Life       | Cost  | Use Case Match (Lighting) |
|---------------|:------------------:|:------------------:|:-----:|:-------------------------:|
| **PIR Sensor**| :x:                | :white_check_mark: | :white_check_mark: | Good (for hallways)       |
| **mmWave Sensor**| :white_check_mark: | :x:                | :x:   | Excellent (for rooms)     |

### Conclusion on Item Type

A hybrid strategy is the optimal approach for sensors.

*   **For primary rooms (living room, office, bedroom):** **mmWave sensors** are the best choice to achieve true presence detection and prevent lights from turning off unexpectedly.
*   **For transient spaces (hallways, closets, bathrooms):** **PIR sensors** are the most practical and cost-effective solution, as people are generally only moving through these areas.

---

## Phase 4: Choosing the Specific *Product*

*(This section will be populated with specific recommendations for PIR sensors (e.g., Aqara P1), mmWave sensors (e.g., Aqara FP2), and contact sensors.)*

---

## Phase 5: Post-Purchase Guide

*(This section will detail pairing with Home Assistant and best practices for placement to maximize effectiveness and minimize false positives.)*

---

## Phase 6: Essential Accessories & Add-Ons

*(This section will cover mounting options and, for mmWave sensors, appropriate USB power supplies.)*

---

## Sources & Further Reading

*(A list of resources will be added here, including in-depth comparisons and reviews from smart home technology channels.)* 