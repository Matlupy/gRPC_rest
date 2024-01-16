from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MerchantId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Merchant(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FullMerchant(_message.Message):
    __slots__ = ("id", "name", "customer_id", "transact_amount", "check_fraud", "age", "gender", "zipcode_ori", "zipcode_dest", "category")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CHECK_FRAUD_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    ZIPCODE_ORI_FIELD_NUMBER: _ClassVar[int]
    ZIPCODE_DEST_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    customer_id: str
    transact_amount: float
    check_fraud: int
    age: int
    gender: str
    zipcode_ori: str
    zipcode_dest: str
    category: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., customer_id: _Optional[str] = ..., transact_amount: _Optional[float] = ..., check_fraud: _Optional[int] = ..., age: _Optional[int] = ..., gender: _Optional[str] = ..., zipcode_ori: _Optional[str] = ..., zipcode_dest: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...
