---
title: "Smart LED Strips"
description: "Researching and comparing smart LED strips to find the best options for high-quality, responsive, and locally-controlled accent and task lighting."
tags:
  - item
  - item-category:home_automation
  - research
  - comparison
  - corner:bazaar
  - type:blogpost
  - lighting
  - led-strip
  - zigbee
  - addressable-led
---

# Smart LED Strips

Smart LED strips are a versatile tool for both functional and aesthetic lighting, capable of providing everything from under-cabinet task lighting to dynamic, colorful accent lighting. My goal is to find high-quality LED strips that offer excellent color accuracy, can be controlled locally through Home Assistant, and are suitable for various DIY and pre-packaged applications.

---

## Phase 1: Researching the Field

### Keywords, Terms and Concepts

1.  **LED Strip Types**
    *   **Non-Addressable (Analog) Strips:** The entire strip is one color at a time. You can change the color and brightness of the whole strip, but not parts of it. These are simple and good for uniform, single-color lighting (e.g., under-cabinet).
    *   **Addressable (Digital) Strips:** Each LED (or a small group of LEDs) can be controlled individually. This allows for complex gradients, animations, and effects. This is the technology behind products like Govee and is heavily used in the DIY community with controllers like WLED.
2.  **Light Quality & Performance**
    *   **CRI (Color Rendering Index):** Just as with bulbs, a CRI of 90+ is crucial for any white light application to ensure colors look natural.
    *   **LED Density:** Measured in LEDs per meter. Higher density (e.g., 60+ LEDs/m) results in more uniform light with fewer visible "dots" or hotspots. Lower density is cheaper but can look spotty.
    *   **IP Rating:** Indicates the level of protection against solids and liquids. IP20 is for indoor, dry locations. IP65 has a silicone coating for splash resistance. IP67/68 is for more water-resistant applications.
3.  **Technology & Control**
    *   **Zigbee/Wi-Fi Controllers:** Pre-packaged LED strips often come with a built-in Zigbee or Wi-Fi controller (e.g., Philips Hue Lightstrip). These are easy to set up but less flexible.
    *   **DIY Addressable Controllers (WLED):** For maximum control over addressable strips, the DIY community standard is WLED. This is open-source firmware that runs on an ESP32 microcontroller, giving you incredibly powerful web-based control and effects, plus seamless integration with Home Assistant.
    *   **Power Injection:** For long runs of LED strips, the voltage can drop, causing colors to be inaccurate at the far end of the strip. Power injection involves running additional power wires to points further down the strip to maintain consistent voltage and color.
4.  **LED Chip Types**
    *   **SK6812:** A popular type of addressable LED. Notably, it comes in an **RGBW** variant, which includes a dedicated white channel for much higher quality white light than standard RGB LEDs (like the WS2812B).
    *   **WS2812B:** A very common and cheap **RGB** addressable LED. Good for colorful effects but poor for producing white light.

### Guiding Questions

1.  **Addressable vs. Non-Addressable: Which do I need?**
    For simple, uniform under-cabinet or cove lighting, a non-addressable strip is sufficient and cheaper. For any dynamic effects, gradients, or media-syncing (e.g., bias lighting for a TV), addressable strips are required.
2.  **What is WLED and why is it so popular?**
    WLED is a free and open-source firmware for ESP32 boards that turns them into best-in-class controllers for addressable LED strips. It offers a rich web UI, hundreds of effects, and direct integration with Home Assistant. It represents the pinnacle of DIY lighting control.
3.  **Why is a dedicated white channel (like in SK6812 RGBW) important?**
    Standard RGB LEDs create white by mixing red, green, and blue at full brightness. This results in a low-CRI, often blue- or pink-tinted "white." A dedicated white LED produces a much cleaner, higher-quality, and more efficient white light, making it suitable for functional task lighting, not just colorful effects.

---

## Phase 2: Defining My Needs & Priorities

*(This section will be populated based on specific use cases, such as under-cabinet lighting, TV bias lighting, or architectural accent lighting.)*

---

## Phase 3: Comparing & Choosing the Item *Type*

*(This section will compare pre-packaged solutions like Philips Hue vs. DIY solutions with WLED, based on cost, flexibility, and ease of setup.)*

---

## Phase 4: Choosing the Specific *Product*

*(This section will be populated with specific recommendations for LED strips (e.g., BTF-LIGHTING), controllers (e.g., QuinLED), and power supplies.)*

---

## Phase 5: Post-Purchase Guide

*(This section will detail assembly, wiring, power injection, and configuring WLED for Home Assistant.)*

---

## Phase 6: Essential Accessories & Add-Ons

*(This section will cover recommendations for aluminum channels with diffusers, connectors, and appropriate wiring.)*

---

## Sources & Further Reading

*(A list of resources will be added here, including guides from The Hook Up and other DIY lighting experts.)*
