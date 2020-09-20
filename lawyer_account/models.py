from django.db import models
from django.contrib.auth.models import User
from .BigViriables import bar_chambers


class LawFirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_law_firm = models.CharField(max_length=100,
                                     verbose_name='Название фирмы')
    firstname_general_manager = models.CharField(max_length=100,
                                                 verbose_name='Имя генерального директора')
    lastname_general_manager = models.CharField(max_length=100,
                                                verbose_name='Фамилия генерального директора')
    patronymic_general_manager = models.CharField(max_length=100,
                                                  verbose_name='Отчество генерального директора',
                                                  null=True,
                                                  default='',
                                                  blank=True)
    constituent_document = models.CharField(max_length=100,
                                            verbose_name='Учредительный документ',
                                            null=True,
                                            blank=True,
                                            choices=[('Устав', 'Устав'),
                                                     ('Типовой устав', 'Типовой устав'),
                                                     ('Учредительный договор', 'Учредительный договор')])
    date_of_approval_of_the_constituent_document = models.DateField(blank=True,
                                                                    null=True,
                                                                    verbose_name='Дата утверждения учредительного документа')
    organizational_and_legal_form = models.CharField(max_length=100,
                                                     verbose_name='Организационно-правовая форма')
    main_state_registration_number = models.IntegerField(blank=True,
                                                         null=True,
                                                         verbose_name='Основной государственный регистрационный номер')
    taxpayer_identification_number = models.CharField(max_length=100,
                                                      blank=True,
                                                      null=True,
                                                      verbose_name='Идентификационный номер налогоплательщика')
    code_of_the_reason_for_registration = models.CharField(max_length=30,
                                                           null=True,
                                                           blank=True,
                                                           verbose_name='Код причины постановки на учет')
    payment_account = models.CharField(max_length=20,
                                       verbose_name='Расчетный счет',
                                       blank=True,
                                       null=True)
    servicing_bank = models.CharField(max_length=50,
                                      verbose_name='Обслуживающий банк',
                                      blank=True,
                                      null=True)
    bank_identification_code = models.CharField(max_length=9,
                                                verbose_name='Банковский индификационный код',
                                                blank=True,
                                                null=True)
    # Адрес
    legal_address = models.CharField(max_length=200,
                                     verbose_name='Юридический адрес',
                                     null=True,
                                     blank=True)
    actual_address = models.CharField(max_length=200,
                                      verbose_name='Фактический адрес',
                                      null=True,
                                      blank=True)

    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    phone_number = models.CharField(max_length=11,
                                    verbose_name='Номер телефона',
                                    blank=True,
                                    null=True,
                                    default='')
    # Специализация
    all_branches_of_law = models.BooleanField(default=False, verbose_name='Все отрасли права')

    civil_law = models.BooleanField(default=False, verbose_name='Гражданское право')
    experience_in_civil_law = models.DateField(blank=True,
                                               null=True,
                                               verbose_name='Опыт в гражданском праве')

    criminal_law = models.BooleanField(default=False, verbose_name='Уголовное право')
    experience_in_criminal_law = models.DateField(blank=True,
                                                  null=True,
                                                  verbose_name='Опыт в уголовном праве')

    housing_law = models.BooleanField(default=False, verbose_name='Жилищное право')
    experience_in_housing_law = models.DateField(blank=True,
                                                 null=True,
                                                 verbose_name='Опыт в жилищном праве')

    labour_law = models.BooleanField(default=False, verbose_name='Трудовое право')
    experience_in_labour_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в трудовом праве')

    tax_law = models.BooleanField(default=False, verbose_name='Налоговое право')
    experience_in_tax_law = models.DateField(blank=True,
                                             null=True,
                                             verbose_name='Опыт в налоговом праве')

    municipal_law = models.BooleanField(default=False, verbose_name='Муниципальное право')
    experience_in_municipal_law = models.DateField(blank=True,
                                                   null=True,
                                                   verbose_name='Опыт в муниципальном праве')

    family_law = models.BooleanField(default=False, verbose_name='Семейное право')
    experience_in_family_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в семейном праве')


class IndividualEntrepreneurLawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100,
                                  verbose_name='Имя',
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия',
                                 null=True,
                                 blank=True)
    patronymic = models.CharField(max_length=100,
                                  verbose_name='Отчество',
                                  null=True,
                                  blank=True)

    address_of_registration_of_an_individual_entrepreneur = models.CharField(max_length=200,
                                                                             verbose_name='Адресс регистрации ИП',
                                                                             null=True,
                                                                             blank=True)
    main_state_registration_number_individual_entrepreneur = models.IntegerField(null=True,
                                                                                 blank=True,
                                                                                 verbose_name='Основной государственный регистрационный номер ИП')
    taxpayer_identification_number = models.CharField(max_length=100,
                                                      blank=True,
                                                      null=True,
                                                      verbose_name='Идентификационный номер налогоплательщика')
    number_of_the_registration_certificate = models.CharField(max_length=20,
                                                              null=True,
                                                              blank=True,
                                                              verbose_name='Номер свидетельства о постановке на учет')
    Date_of_approval_of_the_registration_certificate = models.DateField(blank=True,
                                                                        null=True,
                                                                        verbose_name='Дата свидетельства о постановке на учет')
    phone_number = models.CharField(max_length=11,
                                    verbose_name='Номер телефона',
                                    default='',
                                    blank=True,
                                    null=True)
    bank_identification_code = models.CharField(max_length=9,
                                                verbose_name='Банковский индификационный код',
                                                blank=True,
                                                null=True)
    availability_of_office_space = models.BooleanField(default=False,
                                                       verbose_name="Наличие офисного помещения")
    address_office_space = models.CharField(max_length=200,
                                            verbose_name='Адресс офисного помещения',
                                            null=True,
                                            blank=True)
    availability_of_employees = models.BooleanField(default=False,
                                                    verbose_name='Наличие работников')
    payment_account = models.CharField(max_length=20,
                                       verbose_name='Расчетный счет',
                                       blank=True,
                                       null=True)
    servicing_bank = models.CharField(max_length=50,
                                      verbose_name='Обслуживающий банк',
                                      blank=True,
                                      null=True)

    # Специализация
    all_branches_of_law = models.BooleanField(default=False, verbose_name='Все отрасли права')

    civil_law = models.BooleanField(default=False, verbose_name='Гражданское право')
    experience_in_civil_law = models.DateField(blank=True,
                                               null=True,
                                               verbose_name='Опыт в гражданском праве')

    criminal_law = models.BooleanField(default=False, verbose_name='Уголовное право')
    experience_in_criminal_law = models.DateField(blank=True,
                                                  null=True,
                                                  verbose_name='Опыт в уголовном праве')

    housing_law = models.BooleanField(default=False, verbose_name='Жилищное право')
    experience_in_housing_law = models.DateField(blank=True,
                                                 null=True,
                                                 verbose_name='Опыт в жилищном праве')

    labour_law = models.BooleanField(default=False, verbose_name='Трудовое право')
    experience_in_labour_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в трудовом праве')

    tax_law = models.BooleanField(default=False, verbose_name='Налоговое право')
    experience_in_tax_law = models.DateField(blank=True,
                                             null=True,
                                             verbose_name='Опыт в налоговом праве')

    municipal_law = models.BooleanField(default=False, verbose_name='Муниципальное право')
    experience_in_municipal_law = models.DateField(blank=True,
                                                   null=True,
                                                   verbose_name='Опыт в муниципальном праве')

    family_law = models.BooleanField(default=False, verbose_name='Семейное право')
    experience_in_family_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в семейном праве')


class BranchLawFirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    name_branch_law_firm = models.CharField(max_length=100,
                                            verbose_name='Наименование филиала',
                                            null=True,
                                            blank=True)
    name_main_law_firm = models.CharField(max_length=100,
                                          verbose_name='Наименование головной организации',
                                          null=True,
                                          blank=True)
    firstname_general_manager = models.CharField(max_length=100,
                                                 verbose_name='Имя директора филиала',
                                                 null=True,
                                                 blank=True)
    lastname_general_manager = models.CharField(max_length=100,
                                                verbose_name='Фамилия директора филиала',
                                                null=True,
                                                blank=True)
    patronymic_general_manager = models.CharField(max_length=100,
                                                  verbose_name='Отчество директора филиала',
                                                  null=True,
                                                  blank=True)
    actual_address = models.CharField(max_length=200,
                                      verbose_name='Фактический адрес филиала',
                                      null=True,
                                      blank=True)
    servicing_bank = models.CharField(max_length=50,
                                      verbose_name='Обслуживающий банк',
                                      blank=True,
                                      null=True)
    payment_account = models.CharField(max_length=20,
                                       verbose_name='Расчетный счет',
                                       blank=True,
                                       null=True)
    taxpayer_identification_number = models.CharField(max_length=100,
                                                      blank=True,
                                                      null=True,
                                                      verbose_name='Идентификационный номер налогоплательщика')
    date_of_the_power_of_attorney = models.DateField(blank=True,
                                                     null=True,
                                                     verbose_name='Дата совершения доверенности')
    main_state_registration_number = models.IntegerField(blank=True,
                                                         null=True,
                                                         verbose_name='Основной государственный регистрационный номер')
    code_of_the_reason_for_registration = models.CharField(max_length=30,
                                                           null=True,
                                                           blank=True,
                                                           verbose_name='Код причины постановки на учет')
    bank_identification_code = models.CharField(max_length=9,
                                                verbose_name='Банковский индификационный код',
                                                blank=True,
                                                null=True)
    phone_number = models.CharField(max_length=11,
                                    verbose_name='Номер телефона филиала',
                                    blank=True,
                                    null=True)

    # Специализация
    all_branches_of_law = models.BooleanField(default=False, verbose_name='Все отрасли права')

    civil_law = models.BooleanField(default=False, verbose_name='Гражданское право')
    experience_in_civil_law = models.DateField(blank=True,
                                               null=True,
                                               verbose_name='Опыт в гражданском праве')

    criminal_law = models.BooleanField(default=False, verbose_name='Уголовное право')
    experience_in_criminal_law = models.DateField(blank=True,
                                                  null=True,
                                                  verbose_name='Опыт в уголовном праве')

    housing_law = models.BooleanField(default=False, verbose_name='Жилищное право')
    experience_in_housing_law = models.DateField(blank=True,
                                                 null=True,
                                                 verbose_name='Опыт в жилищном праве')

    labour_law = models.BooleanField(default=False, verbose_name='Трудовое право')
    experience_in_labour_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в трудовом праве')

    tax_law = models.BooleanField(default=False, verbose_name='Налоговое право')
    experience_in_tax_law = models.DateField(blank=True,
                                             null=True,
                                             verbose_name='Опыт в налоговом праве')

    municipal_law = models.BooleanField(default=False, verbose_name='Муниципальное право')
    experience_in_municipal_law = models.DateField(blank=True,
                                                   null=True,
                                                   verbose_name='Опыт в муниципальном праве')

    family_law = models.BooleanField(default=False, verbose_name='Семейное право')
    experience_in_family_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в семейном праве')


class MemberOfTheBarChamber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100,
                                  verbose_name='Имя',
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия',
                                 null=True,
                                 blank=True)
    patronymic = models.CharField(max_length=100,
                                  verbose_name='Отчество',
                                  null=True,
                                  blank=True)

    bar_chamber = models.CharField(max_length=100,
                                   verbose_name='Адвокатская палата',
                                   null=True,
                                   blank=True,
                                   choices=bar_chambers)
    bar_association = models.CharField(max_length=100,
                                       verbose_name='Член адвокатского образования',
                                       null=True,
                                       blank=True,
                                       choices=[('Адвокатский кабинет', 'Адвокатский кабинет'),
                                                ('Адвокатская коллегия', 'Адвокатская коллегия'),
                                                ('Адвокатское бюро', 'Адвокатское бюро')])
    name_of_the_bar_association = models.CharField(max_length=200,
                                                   verbose_name='Наименование адвокатского образования',
                                                   null=True,
                                                   blank=True)
    registration_number = models.CharField(max_length=20,
                                           verbose_name='Регистрационный номер',
                                           null=True,
                                           blank=True)
    certificates_number = models.CharField(max_length=20,
                                           null=True,
                                           blank=True,
                                           verbose_name='Номер удостоверения')
    date_of_issue_certificates = models.DateField(null=True,
                                                  blank=True,
                                                  verbose_name='Дата выдачи удостоверения')
    authority_that_issued_the_certificate = models.CharField(max_length=50,
                                                             null=True,
                                                             blank=True,
                                                             verbose_name='Орган, выдавший удостоверение')
    phone_number = models.CharField(max_length=11,
                                    verbose_name='Номер телефона',
                                    blank=True,
                                    null=True)
    payment_account = models.CharField(max_length=20,
                                       verbose_name='Расчетный счет',
                                       blank=True,
                                       null=True)
    servicing_bank = models.CharField(max_length=50,
                                      verbose_name='Обслуживающий банк',
                                      blank=True,
                                      null=True)
    bank_identification_code = models.CharField(max_length=9,
                                                verbose_name='Банковский индификационный код',
                                                blank=True,
                                                null=True)
    availability_of_office_space = models.BooleanField(default=False,
                                                       verbose_name="Наличие офисного помещения")
    address = models.CharField(max_length=200,
                               verbose_name='Адресс офисного помещения',
                               null=True,
                               blank=True)

    # Специализация
    all_branches_of_law = models.BooleanField(default=False, verbose_name='Все отрасли права')

    civil_law = models.BooleanField(default=False, verbose_name='Гражданское право')
    experience_in_civil_law = models.DateField(blank=True,
                                               null=True,
                                               verbose_name='Опыт в гражданском праве')

    criminal_law = models.BooleanField(default=False, verbose_name='Уголовное право')
    experience_in_criminal_law = models.DateField(blank=True,
                                                  null=True,
                                                  verbose_name='Опыт в уголовном праве')

    housing_law = models.BooleanField(default=False, verbose_name='Жилищное право')
    experience_in_housing_law = models.DateField(blank=True,
                                                 null=True,
                                                 verbose_name='Опыт в жилищном праве')

    labour_law = models.BooleanField(default=False, verbose_name='Трудовое право')
    experience_in_labour_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в трудовом праве')

    tax_law = models.BooleanField(default=False, verbose_name='Налоговое право')
    experience_in_tax_law = models.DateField(blank=True,
                                             null=True,
                                             verbose_name='Опыт в налоговом праве')

    municipal_law = models.BooleanField(default=False, verbose_name='Муниципальное право')
    experience_in_municipal_law = models.DateField(blank=True,
                                                   null=True,
                                                   verbose_name='Опыт в муниципальном праве')

    family_law = models.BooleanField(default=False, verbose_name='Семейное право')
    experience_in_family_law = models.DateField(blank=True,
                                                null=True,
                                                verbose_name='Опыт в семейном праве')
