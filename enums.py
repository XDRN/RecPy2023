from enum import Enum

class roomJoinErrorCodes(Enum):
    UnknownError = -1
    Success = 0
    NoSuchGame = 1
    PlayerNotOnline = 2
    InsufficientSpace = 3
    EventNotStarted = 4
    EventAlreadyFinished = 5
    BlockedFromRoom = 7
    JuniorNotAllowed = 11
    Banned = 12
    AlreadyInBestInstance = 13
    InsufficientRelationship = 14
    UpdateRequired = 16
    AlreadyInTargetInstance = 17
    UGCNotAllowed = 19
    NoSuchRoom = 20
    RoomIsNotActive = 22
    RoomBlockedByCreator = 23
    RoomIsPrivate = 25
    RoomInstanceIsPrivate = 26
    DeviceClassNotSupported = 30
    DeviceClassNotSupportedByRoomOwner = 31
    MovementModeNotSupportedByRoomOwner = 32
    EventIsPrivate = 35
    EventIsFull = 36
    RoomInviteExpired = 40
    NoAvailableRegion = 45
    NotorietyTooPoor = 50
    BannedFromRoom = 55
    NoSuchClub = 70
    ClubHasNoClubhouse = 71
    ClubIsNotActive = 73
    NotAMemberOfClub = 74
    BannedFromClub = 75
    InstanceJoinNotPermitted = 76
    LevelTooLow = 77
    ChatPartyInviteNotFound = 78
    ChatPartyInviteModerated = 79
    ChatMessageNotAnInvite = 80
    DeveloperOnly = 81
    RRPlusRequired = 82
    MetaJuniorAccountRestriction = 83
    NotExclusivelyLoggedIn = 84
    AccountDoesNotExist = 85

class roomRoles(Enum):
    None_ = 0
    Banned = 1
    Host = 10
    Moderator = 20
    CoOwner = 30
    TemporaryCoOwner = 31
    Creator = 255