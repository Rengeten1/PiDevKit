# Raspberry Pi OS Installation Guide

## Prerequisites
- Raspberry Pi Zero 2 W
- MicroSD card (16GB or larger, Class 10 recommended)
- MicroSD card reader
- Computer with internet connection
- Micro USB cable for power
- HDMI cable and monitor (optional)

## Step 1: Download Raspberry Pi Imager
1. Visit the official Raspberry Pi website: https://www.raspberrypi.org/software/
2. Download Raspberry Pi Imager for your operating system
3. Install the application

## Step 2: Prepare the SD Card
1. Insert your microSD card into the card reader
2. Connect the card reader to your computer
3. Launch Raspberry Pi Imager

## Step 3: Flash the OS
1. Click "Choose OS" and select "Raspberry Pi OS (32-bit)"
2. Click "Choose Storage" and select your SD card
3. Click the gear icon (⚙️) for advanced options:
    - Enable SSH (optional)
    - Set username and password
    - Configure Wi-Fi credentials
    - Set locale settings
4. Click "Write" to flash the OS
5. Wait for the process to complete

## Step 4: Boot Your Raspberry Pi
1. Insert the flashed SD card into your Raspberry Pi Zero 2 W
2. Connect peripherals (keyboard, mouse, monitor)
3. Connect the power cable
4. The Pi will boot automatically

## Step 5: Initial Setup
1. Complete the welcome wizard
2. Update the system:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
3. Reboot if required

## Troubleshooting
- If the Pi doesn't boot, check SD card connections
- Ensure the power supply provides adequate current (5V, 2.5A minimum)
- Verify the OS image was written successfully

Your Raspberry Pi OS installation is now complete!