import asyncio
from bleak import BleakClient

ADDRESS = "36:46:3E:C0:72:29"
CHARACTERISTIC_UUID = "0000ffd9-0000-1000-8000-00805f9b34fb"
TURN_OFF = bytearray([0xCC, 0x24, 0x33])

async def main():
    async with BleakClient(ADDRESS) as client:
        print("Connected:", client.is_connected)
        await client.write_gatt_char(CHARACTERISTIC_UUID, TURN_OFF)
        print("Turned OFF")

if __name__ == "__main__":
    asyncio.run(main())