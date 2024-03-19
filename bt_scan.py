import asyncio
from bleak import BleakClient

async def run(address):
    async with BleakClient(address) as client:
        # デバイスに接続
        connected = await client.is_connected()
        print(f"Connected: {connected}")

        for service in client.services:
            print(f"Service: {service.uuid}")
            for char in service.characteristics:
                if "read" in char.properties:
                    # 特性が読み取り可能な場合、値を読み取る
                    value = bytes(await client.read_gatt_char(char.uuid))
                    print(f"  Characteristic: {char.uuid}, Value: {value}")
                else:
                    print(f"  Characteristic: {char.uuid}, Properties: {char.properties}")

# BLEデバイスのアドレス
address = "BC:10:7B:87:21:5E"

# イベントループを実行
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
