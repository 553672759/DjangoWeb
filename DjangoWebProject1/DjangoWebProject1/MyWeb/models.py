# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MywebVideos(models.Model):
    videoid = models.CharField(db_column='VideoId', primary_key=True, max_length=50)  # Field name made lowercase.
    videotitle = models.CharField(db_column='VideoTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videolink = models.TextField(db_column='VideoLink', blank=True, null=True)  # Field name made lowercase.
    videond = models.CharField(db_column='VideoND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videocontent = models.TextField(db_column='VideoContent', blank=True, null=True)  # Field name made lowercase.
    videopf = models.CharField(db_column='VideoPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videoimgname = models.CharField(db_column='VideoImgName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videotag = models.CharField(db_column='VideoTag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videoimg = models.CharField(db_column='VideoImg', max_length=255, blank=True, null=True)  # Field name made lowercase.

    #打印对象时，会打印videotitle
    def __str__(self):
        return self.videotitle

    class Meta:
        managed = False
        db_table = 'MyWeb_Videos'


class MywebDblist(models.Model):
    daiban = models.CharField(max_length=255)
    yiwancheng = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'MyWeb_dblist'


class MywebWenzhang(models.Model):
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'MyWeb_wenzhang'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
