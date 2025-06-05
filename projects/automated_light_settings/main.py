import asyncio
from bleak import BleakClient
from data import get_today_sunset
from time_utils import get_current_utc_time

ADDRESS = "36:46:3E:C0:72:29"
CHARACTERISTIC_UUID = "0000ffd9-0000-1000-8000-00805f9b34fb"

TURN_ON = bytearray([0xCC, 0x23, 0x33])
TURN_OFF = bytearray([0xCC, 0x24, 0x33])
MY_COLOR = bytearray([0x56, 255, 50, 0, 255, 0xAA])

async def turn_light_on():
    async with BleakClient(ADDRESS) as client:
        print("Connected:", client.is_connected)
        await asyncio.sleep(1)
        await client.write_gatt_char(CHARACTERISTIC_UUID, TURN_ON)
        print("Turned ON")
        await asyncio.sleep(0.1)
        await client.write_gatt_char(CHARACTERISTIC_UUID, MY_COLOR)
        print("Set My Color")

async def main():
    sunset_time = get_today_sunset()
    current_time = get_current_utc_time()
    print(f"Current UTC time: {current_time}")
    print(f"Today's sunset (UTC): {sunset_time}")

    if current_time > sunset_time:
        await turn_light_on()
    else:
        print("It's not sunset yet.")

if __name__ == "__main__":
    asyncio.run(main())