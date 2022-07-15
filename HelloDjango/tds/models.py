from django.db import models

class My_settings (models.Model ):
    setname = models.CharField(max_length=25, default='', blank=False)
    value = models.CharField(max_length=255, default='', blank=True)
    descr = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return f"{self.setname} = {self.value} , #{self.descr}"

class Dogovor (models.Model):
    dog_id = models.CharField(max_length=10, default='', blank=True)
    CONTR_NUM = models.CharField(max_length=10, default='', blank=True)
    UL = models.CharField(max_length=50, default='', blank=True)
    DOM = models.CharField(max_length=5, default='', blank=True)
    KORPUS = models.CharField(max_length=5, default='', blank=True)
    PODEZD = models.CharField(max_length=5, default='', blank=True)
    KVARTIRA = models.CharField(max_length=5, default='', blank=True)
    TEL = models.CharField(max_length=20, default='', blank=True)
    SMOTRITEL = models.CharField(max_length=50, default='', blank=True)
    D_BEGIN = models.CharField(max_length=20, default='', blank=True)
    D_END = models.CharField(max_length=20, default='', blank=True)
    REMONTNIK = models.CharField(max_length=50, default='', blank=True)
    PRODLENIE = models.CharField(max_length=1, default='', blank=True)
    ADDED_ON = models.CharField(max_length=20, default='', blank=True)
    PRIMECHANIE = models.CharField(max_length=150, default='', blank=True)
    Key_num = models.CharField(max_length=10, default='', blank=True)
    Sys_pass = models.CharField(max_length=10, default='', blank=True)
    Lock_pass = models.CharField(max_length=10, default='', blank=True)
    Tbv = models.CharField(max_length=10, default='', blank=True)
    Tbv2 = models.CharField(max_length=10, default='', blank=True)
    TZ = models.CharField(max_length=10, default='', blank=True)
    From_to = models.CharField(max_length=100, default='', blank=True)
    No_serv = models.CharField(max_length=500, default='', blank=True)
    Manager = models.CharField(max_length=150, default='', blank=True)
    Kv_count = models.CharField(max_length=10, default='', blank=True)
    org = models.CharField(max_length=50, default='', blank=True)
    spetsobslug = models.CharField(max_length=150, default='', blank=True)
    kod_open_close = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return f'{self.CONTR_NUM}, {self.UL}, {self.DOM}к{self.KORPUS},п{self.PODEZD} # {self.kod_open_close} '

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
