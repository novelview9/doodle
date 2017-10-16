from peewee import *
import datetime
from custom_fields import CustomTimestampField

database = SqliteDatabase('database.sqlite', **{})

class BaseModel(Model):
    class Meta:
        database = database


class Zsfnote(BaseModel):
    zarchived = IntegerField(db_column='ZARCHIVED', null=True)
    zarchiveddate = TextField(db_column='ZARCHIVEDDATE', null=True)  # TIMESTAMP
    zcreationdate = CustomTimestampField(db_column='ZCREATIONDATE', null=True)  # TIMESTAMP
    zencrypted = IntegerField(db_column='ZENCRYPTED', null=True)
    zfolder = IntegerField(db_column='ZFOLDER', index=True, null=True)
    zhasfiles = IntegerField(db_column='ZHASFILES', null=True)
    zhasimages = IntegerField(db_column='ZHASIMAGES', null=True)
    zhassourcecode = IntegerField(db_column='ZHASSOURCECODE', null=True)
    zlasteditingdevice = TextField(db_column='ZLASTEDITINGDEVICE', null=True)  # VARCHAR
    zlocked = IntegerField(db_column='ZLOCKED', null=True)
    zlockeddate = TextField(db_column='ZLOCKEDDATE', null=True)  # TIMESTAMP
    zmodificationdate = TextField(db_column='ZMODIFICATIONDATE', null=True)  # TIMESTAMP
    zorder = IntegerField(db_column='ZORDER', null=True)
    zorderdate = TextField(db_column='ZORDERDATE', null=True)  # TIMESTAMP
    zpermanentlydeleted = IntegerField(db_column='ZPERMANENTLYDELETED', null=True)
    zpinned = IntegerField(db_column='ZPINNED', null=True)
    zpinneddate = TextField(db_column='ZPINNEDDATE', null=True)  # TIMESTAMP
    zshownintodaywidget = IntegerField(db_column='ZSHOWNINTODAYWIDGET', null=True)
    zskipsync = IntegerField(db_column='ZSKIPSYNC', null=True)
    zsubtitle = TextField(db_column='ZSUBTITLE', null=True)  # VARCHAR
    ztext = TextField(db_column='ZTEXT', null=True)  # VARCHAR
    ztitle = TextField(db_column='ZTITLE', null=True)  # VARCHAR
    ztodocompleted = IntegerField(db_column='ZTODOCOMPLETED', null=True)
    ztodoincompleted = IntegerField(db_column='ZTODOINCOMPLETED', null=True)
    ztrashed = IntegerField(db_column='ZTRASHED', null=True)
    ztrasheddate = TextField(db_column='ZTRASHEDDATE', null=True)  # TIMESTAMP
    zuniqueidentifier = TextField(db_column='ZUNIQUEIDENTIFIER', null=True)  # VARCHAR
    zvectorclock = BlobField(db_column='ZVECTORCLOCK', null=True)
    z_ent = IntegerField(db_column='Z_ENT', null=True)
    z_opt = IntegerField(db_column='Z_OPT', null=True)
    z_pk = PrimaryKeyField(db_column='Z_PK', null=True)

    class Meta:
        db_table = 'ZSFNOTE'

class ZPrimarykey(BaseModel):
    z_ent = PrimaryKeyField(db_column='Z_ENT', null=True)
    z_max = IntegerField(db_column='Z_MAX', null=True)
    z_name = TextField(db_column='Z_NAME', null=True)  # VARCHAR
    z_super = IntegerField(db_column='Z_SUPER', null=True)

    class Meta:
        db_table = 'Z_PRIMARYKEY'
