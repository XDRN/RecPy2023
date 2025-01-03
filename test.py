

from RecNet import room_API


print("INT")
room_API.init()

room_API.loadRooms("AGRoomRuntimeConfig.json")

print(room_API.rooms)