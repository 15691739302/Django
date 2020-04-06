# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class SchoolBaseInfo(models.Model):
    school_name = models.CharField(max_length=255)
    school_id = models.IntegerField()
    logo = models.CharField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    old_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    short = models.CharField(max_length=255, blank=True, null=True)
    num_doctor = models.CharField(max_length=255, blank=True, null=True)
    num_master = models.CharField(max_length=255, blank=True, null=True)
    num_subject = models.CharField(max_length=255, blank=True, null=True)
    num_lab = models.CharField(max_length=255, blank=True, null=True)
    num_library = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_base_info'


class SchoolComment(models.Model):
    school_id = models.IntegerField()
    nickname = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    comprehensive_score = models.CharField(max_length=255, blank=True, null=True)
    comment_time = models.CharField(max_length=100, blank=True, null=True)
    like_num = models.IntegerField(blank=True, null=True)
    point_num = models.IntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_comment'


class SchoolContractArea(models.Model):
    school_id = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    rate = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_contract_area'


class SchoolLowestScore(models.Model):
    school_id = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_lowest_score'


class SchoolProvinceline(models.Model):
    school_id = models.IntegerField()
    year = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    highest_score = models.CharField(max_length=255, blank=True, null=True)
    average_score = models.CharField(max_length=255, blank=True, null=True)
    lowest_score = models.CharField(max_length=255, blank=True, null=True)
    lowest_rank = models.CharField(max_length=255, blank=True, null=True)
    provincial_line = models.CharField(max_length=255, blank=True, null=True)
    admission_type = models.CharField(max_length=255, blank=True, null=True)
    admission_lot = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_provinceline'


class SchoolRank(models.Model):
    school_id = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    rank_type = models.IntegerField(blank=True, null=True)
    view_month = models.IntegerField(blank=True, null=True)
    view_week = models.IntegerField(blank=True, null=True)
    level_name = models.CharField(max_length=255, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    f211 = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    province_name = models.CharField(max_length=255, blank=True, null=True)
    nature_name = models.CharField(max_length=255, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    f985 = models.IntegerField(blank=True, null=True)
    dual_class_name = models.CharField(max_length=255, blank=True, null=True)
    view_total_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_rank'


class SchoolSpecial(models.Model):
    school_id = models.IntegerField(blank=True, null=True)
    special_type = models.CharField(max_length=255, blank=True, null=True)
    special_detail = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_special'


class SchoolUnitNature(models.Model):
    school_id = models.IntegerField(primary_key=True)
    unit_nature = models.CharField(max_length=2000, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_unit_nature'
