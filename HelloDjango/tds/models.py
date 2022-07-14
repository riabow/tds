from django.db import models

# Create your models here.
class Dogovor (models.Model):
    dog_id = models.CharField(max_length=10, default='')
    CONTR_NUM = models.CharField(max_length=10, default='')
    UL = models.CharField(max_length=50, default='')
    DOM = models.CharField(max_length=5, default='')
    KORPUS = models.CharField(max_length=5, default='')
    PODEZD = models.CharField(max_length=5, default='')
    KVARTIRA = models.CharField(max_length=5, default='')
    TEL = models.CharField(max_length=20, default='')
    SMOTRITEL = models.CharField(max_length=50, default='')
    D_BEGIN = models.CharField(max_length=20, default='')
    D_END = models.CharField(max_length=20, default='')
    REMONTNIK = models.CharField(max_length=50, default='')
    PRODLENIE = models.CharField(max_length=1, default='')
    ADDED_ON = models.CharField(max_length=20, default='')
    PRIMECHANIE = models.CharField(max_length=150, default='')
    Key_num = models.CharField(max_length=8, default='')
    Sys_pass = models.CharField(max_length=4, default='')
    Lock_pass = models.CharField(max_length=4, default='')
    Tbv = models.CharField(max_length=5, default='')
    TZ = models.CharField(max_length=10, default='')
    From_to = models.CharField(max_length=10, default='')
    No_serv = models.CharField(max_length=100, default='')
    Manager = models.CharField(max_length=50, default='')
    Kv_count = models.CharField(max_length=5, default='')
    org = models.CharField(max_length=50, default='')
    spetsobslug = models.CharField(max_length=150, default='')
    kod_open_close = models.CharField(max_length=10, default='')


'''
    [Key_num] [nvarchar](8) NULL,
	[Sys_pass] [nvarchar](4) NULL,
	[Lock_pass] [nvarchar](4) NULL,
	[Tbv] [nvarchar](5) NULL,
	[TZ] [nvarchar](10) NULL,
	[From_to] [nvarchar](10) NULL,
	[No_serv] [ntext] NULL,
	[Manager] [nvarchar](50) NULL,
	[Kv_count] [float] NULL,
	[org] [varchar](50) NULL,
	[spetsobslug] [varchar](250) NULL,

'''

"""
CREATE TABLE [dbo].[DOGOVOR](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CONTR_NUM] [nvarchar](10) NULL,
	[UL] [nvarchar](50) NULL,
	[DOM] [nvarchar](5) NULL,
	[KORPUS] [nvarchar](5) NULL,
	[PODEZD] [nvarchar](5) NULL,
	[KVARTIRA] [nvarchar](5) NULL,
	[TEL] [nvarchar](20) NULL,
	[SMOTRITEL] [nvarchar](50) NULL,
	[D_BEGIN] [smalldatetime] NULL,
	[D_END] [smalldatetime] NULL,
	[REMONTNIK] [nvarchar](50) NULL,
	[PRODLENIE] [nvarchar](1) NULL,
	[ADDED_ON] [smalldatetime] NULL,
	[PRIMECHANIE] [nvarchar](150) NULL,
	[Balans] [float] NULL,
	
	
	[Key_num] [nvarchar](8) NULL,
	[Sys_pass] [nvarchar](4) NULL,
	[Lock_pass] [nvarchar](4) NULL,
	[Tbv] [nvarchar](5) NULL,
	[TZ] [nvarchar](10) NULL,
	[From_to] [nvarchar](10) NULL,
	[No_serv] [ntext] NULL,
	[Manager] [nvarchar](50) NULL,
	[Kv_count] [float] NULL,
	[org] [varchar](50) NULL,
	[spetsobslug] [varchar](250) NULL,
 CONSTRAINT [PK_DOGOVOR] PRIMARY KEY CLUSTERED
"""
