---
title: "Touch Displays for Home Assistant"
description: "Researching and comparing touch display solutions to create a centralized, customizable control panel for a Home Assistant dashboard."
tags:
  - item
  - item-category:home_automation
  - research
  - comparison
  - corner:bazaar
  - type:blogpost
  - display
  - touchscreen
  - dashboard
  - home-assistant
---

# Touch Displays for Home Assistant

A dedicated touch display acts as a centralized command center for a smart home, offering a quick and intuitive way to view statuses and control devices without needing a phone. The goal is to find a touch display solution that can be permanently mounted, is highly customizable, and seamlessly displays a Home Assistant dashboard. It should ideally connect directly with a Home Assistant instance, potentially with hardware like the Home Assistant Yellow.

---

## Phase 1: Researching the Field

### Keywords, Terms and Concepts

1.  **Display Hardware & Technology**
    *   **LCD vs. OLED:** LCD screens are more common and affordable, while OLED screens offer perfect blacks and better contrast, making them look more premium, especially with dark-themed dashboards.
    *   **Power over Ethernet (PoE):** A highly desirable feature for wall-mounted displays. It allows a single Ethernet cable to provide both a stable, wired data connection and power to the device, eliminating the need for a separate power adapter near the display.
    *   **Single-Board Computer (SBC):** A small computer like a Raspberry Pi, which can be connected to a touch display to run a web browser or a specific application. The Home Assistant Yellow is a specialized SBC.
2.  **Software & Dashboard**
    *   **Home Assistant Dashboard:** The standard, customizable user interface within Home Assistant. It's built with "Lovelace" cards that can be arranged to show entities and controls.
    *   **Kiosk Mode:** A feature of many web browsers or dedicated apps that displays a webpage full-screen without any address bars, toolbars, or other interface elements. This is essential for a clean, dedicated dashboard look.
    *   **Fully Kiosk Browser:** A popular Android app that provides fine-grained control for turning a tablet into a dedicated dashboard, including features like motion-activated screen wake-up and remote administration.
3.  **Mounting & Form Factor**
    *   **Wall Mounting:** Solutions range from simple on-wall brackets to more integrated in-wall flush mounts that provide a professional, built-in look.
    *   **Desk Stand:** A simpler option for placing a display on a countertop or desk.

### Guiding Questions

1.  **What's the easiest way to get started?**
    Repurposing an old Android tablet (like a Fire Tablet) is by far the most common and easiest entry point. It's affordable and requires minimal hardware knowledge.
2.  **What are the benefits of a dedicated, open-hardware display?**
    Dedicated displays, especially those with PoE, offer a much cleaner and more professional installation. They are designed for permanent, always-on use and provide a more reliable wired connection compared to Wi-Fi.
3.  **How does the Home Assistant Yellow fit in?**
    The Home Assistant Yellow has a GPIO header, which allows it to directly connect to certain types of Raspberry Pi-compatible touch displays. This creates a compact, all-in-one unit where the server and the display are the same device, though this is only practical if you want your main server to be physically located at the display.

---

## Phase 2: Defining My Needs & Priorities

1.  **Primary Use Case(s):**
    *   Create a permanent, wall-mounted control panel for viewing and interacting with a primary Home Assistant dashboard.
2.  **Key Features Needed:**
    1.  **Display:**
        *   Clear, responsive touchscreen.
        *   Sufficient brightness and good viewing angles.
    2.  **Connectivity & Power:**
        *   A reliable connection to the Home Assistant server. A wired connection (Ethernet/PoE) is highly preferred over Wi-Fi.
        *   A clean power solution suitable for wall mounting (PoE is ideal).
    3.  **Software:**
        *   Must be able to display a Home Assistant dashboard in a full-screen kiosk mode.
        *   High degree of customizability for the displayed dashboard.
3.  **Nice to Have:**
    *   Motion or proximity sensor to wake the screen on approach.
    *   High-contrast OLED screen.
4.  **Deal-breakers:**
    *   Inability to display a standard Home Assistant dashboard.
    *   Reliance on a proprietary, non-local cloud service.
    *   Cluttered installation with visible wires that aren't easily concealable.

---

## Phase 3: Comparing & Choosing the Item *Type*

There are three primary approaches to creating a Home Assistant touch display.

### Available Types

#### 1. Repurposed Consumer Tablet (e.g., Fire Tablet, Android Tablet)

1.  **Pros:**
    *   **Low Cost:** Very affordable, especially if using an old or refurbished device. Fire Tablets are a popular budget choice.
    *   **Easy Software Setup:** Using the Home Assistant Companion app or Fully Kiosk Browser is straightforward.
    *   **Built-in Features:** Comes with a battery, speakers, and often a camera/microphone that can be used to wake the screen.
2.  **Cons:**
    *   **Clunky Power/Mounting:** Wall mounting requires a separate bracket, and powering it requires running a visible USB cable or complex custom wiring.
    *   **Wi-Fi Reliant:** Relies on Wi-Fi, which can be less stable than a wired connection.
    *   **Battery Management:** The battery is a point of failure and can degrade or swell over time with constant charging.

#### 2. Dedicated Open Hardware Display (e.g., Raspberry Pi Display, Waveshare)

1.  **Pros:**
    *   **Professional Installation:** Many models are designed for clean wall mounting, often with PoE for single-cable installation.
    *   **Wired Reliability:** A direct Ethernet connection is the most stable option.
    *   **No Battery:** Designed for 24/7 operation without battery concerns.
2.  **Cons:**
    *   **Higher Cost:** More expensive than a consumer tablet.
    *   **More Complex Setup:** Requires connecting the display to an SBC (like a Raspberry Pi), installing an operating system, and configuring it to launch a browser in kiosk mode.

#### 3. All-in-One Commercial Panel (e.g., Crestron, Control4 - adapted for HA)

1.  **Pros:**
    *   **Premium Hardware:** High-quality, professional-grade hardware designed for home automation.
2.  **Cons:**
    *   **Extremely Expensive:** Orders of magnitude more expensive than other options.
    *   **Proprietary Ecosystem:** Designed to work within their own closed ecosystems. While they can sometimes be made to display a webpage, it's often not their intended use and can be complex to configure.
    *   **Overkill:** Not a practical or cost-effective solution for a standard Home Assistant setup.

### Comparison Table of Types

| Type                      | Ease of Setup      | Installation Cleanliness | Cost  | Reliability | Overall Match |
|---------------------------|:------------------:|:------------------------:|:-----:|:-----------:|:-------------:|
| **Repurposed Tablet**     | :white_check_mark: | :x:                      |:white_check_mark:|             | 2 / 4         |
| **Dedicated Open Hardware** | :x:                | :white_check_mark:       | :x:   |:white_check_mark:| 2 / 4         |
| **Commercial Panel**      | :x:                | :white_check_mark:       | :x:   |:white_check_mark:| 2 / 4         |

### Conclusion on Item Type

This is a choice with two strong, but very different, paths. The best option depends heavily on the trade-off between cost/simplicity and installation quality.

*   **Path A (Recommended for Simplicity & Low Cost):** **Repurposed Tablet**.
*   **Path B (Recommended for Best Integration & Reliability):** **Dedicated Open Hardware**.

Given the desire for a clean, permanent installation that can potentially connect directly to the Home Assistant Yellow, we will proceed with researching **Path B: Dedicated Open Hardware**.

---

## Phase 4: Choosing the Specific *Product*

This path involves choosing two main components: the display itself and a Single-Board Computer (SBC) to run it.

### Product Options: The Display

#### 1. Official Raspberry Pi Touch Display (7-inch)

1.  **Pros:**
    *   **Official Support:** Well-supported by the Raspberry Pi ecosystem and its software.
    *   **Good Quality:** A high-quality IPS display with good viewing angles.
2.  **Cons:**
    *   **No Native PoE:** Does not support PoE out of the box. Achieving a clean, single-cable installation requires complex workarounds like separate PoE splitters, which adds bulk and complexity behind the screen.
3. **Conclusion:** While a good display, the lack of integrated PoE makes it a poor choice for our goal of a clean, professional wall-mounted installation.

#### 2. Waveshare PoE Touch Displays (5-inch to 10-inch)

1.  **Pros:**
    *   **Integrated PoE:** This is the killer feature. A single Ethernet cable provides both power and data, making for an extremely clean installation.
    *   **Variety of Sizes:** Available in multiple sizes to fit different wall spaces and use cases.
    *   **Raspberry Pi Focused:** Designed to have a Raspberry Pi (especially the Compute Module 4, which is in the HA Yellow) mount directly to the back of the display.
2.  **Cons:**
    *   **Higher Cost:** More expensive than the official display, but the cost includes the PoE hardware.
3. **Conclusion:** This is the ideal choice. The integrated PoE and direct mounting for a Raspberry Pi solve the two biggest challenges of a dedicated hardware panel.

### The Hardware Strategy

My choice is the **Waveshare 7-inch PoE Touch Display** driven by a **dedicated Raspberry Pi 4**.

**Reasoning:**
*   **The Display:** The 7-inch Waveshare display is the perfect size for a control panel—large enough to be easily readable and interactive, but small enough to be unobtrusive on a wall. The integrated PoE is the most critical feature for a clean, professional install.
*   **The Driver:** While you *could* connect the display directly to a Home Assistant Yellow, it's highly recommended to use a **separate, dedicated Raspberry Pi 4** to drive the display. This decouples your main Home Assistant server from the display, meaning you can restart or work on your server without taking the panel offline, which is a major benefit for reliability.

---

## Phase 5: Post-Purchase Guide

This guide details setting up a dedicated Raspberry Pi 4 to act as a kiosk for your Home Assistant dashboard.

### 1. Hardware Assembly
*   Mount the Raspberry Pi 4 to the back of the Waveshare display using the included standoffs.
*   Connect the display to the Pi's DSI port (for video) and connect the power pins (for touch and power passthrough from the PoE board).

### 2. OS Installation & Configuration
*   **Install Raspberry Pi OS Lite (64-bit):** Flash this lightweight, command-line-only OS to a high-quality SD card. A full desktop environment is unnecessary overhead.
*   **Basic Setup:** After booting, run `sudo raspi-config` to set your locale, keyboard layout, and enable the SSH server for remote access.
*   **Install Required Software:** Install a minimal window manager and a browser.
    ```bash
    sudo apt update && sudo apt install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox chromium-browser
    ```

### 3. Configure Auto-start Kiosk Mode
*   **Create the Kiosk Script:** Create a file at `/home/pi/kiosk.sh` with the following content. This script disables the screen saver and launches Chromium in kiosk mode, pointing to your Home Assistant instance.
    ```bash
    #!/bin/bash
    xset s noblank
    xset s off
    xset -dpms
    
    unclutter & # Hides the mouse cursor
    sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
    
    /usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://homeassistant.local:8123/
    ```
*   **Make it Executable:** `chmod +x /home/pi/kiosk.sh`
*   **Auto-start on Boot:** Edit the `~/.profile` file and add this line to the end: `[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx /home/pi/kiosk.sh`
*   Reboot the Raspberry Pi. It should now boot directly into your Home Assistant dashboard.

---

## Phase 6: Essential Accessories & Add-Ons

### 1. PoE Power Source
*   **Requirement:** The display requires power from a PoE-capable device conforming to the 802.3af standard.
*   **Option A: PoE Switch:** If you have multiple PoE devices, a network switch with built-in PoE ports is the cleanest solution.
*   **Option B: PoE Injector:** If this is your only PoE device, a simple PoE injector is a more cost-effective choice. It sits between your regular switch and the display, adding power to the Ethernet cable.
*   **Recommendation:** A single-port PoE+ injector from a brand like TP-Link or Ubiquiti.

### 2. Wall Mount
*   **Recommendation:** The Waveshare display is often designed to be mounted to a standard single-gang or double-gang electrical box. A simple "low-voltage cutout bracket" is the easiest way to install this in drywall.

### 3. Ethernet Cable
*   **Requirement:** A standard Cat5e or Cat6 Ethernet cable of the appropriate length to run from your switch/injector to the wall-mounted display.

---

## Sources & Further Reading

### Community Guides & Tutorials
1.  **Home Assistant Kiosk Controller - The Right Way**
    *   *Note:* A popular and detailed guide that covers the principles of setting up a Raspberry Pi-based kiosk.
2.  **Waveshare Product Wiki**
    *   *Note:* The official documentation from Waveshare, providing specific details on hardware connections and dimensions for their displays. 

https://youtu.be/gpyYCTgJO88?si=rcAogH451g5HjTA4
https://www.reddit.com/r/homeassistant/comments/17rahys/what_is_everyone_using_for_a_mounted_display/