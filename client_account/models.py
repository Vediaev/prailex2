from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class NaturalPerson(models.Model):  # Добавить остальные позиции
    is_natural_person_profile = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    first_name = models.CharField(max_length=100,
                                  verbose_name='Имя',
                                  blank=True)
    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия',
                                 blank=True)
    patronymic = models.CharField(max_length=100,
                                  verbose_name='Отчество',
                                  blank=True)

    # Паспортные данные
    passport_data_number = models.IntegerField(blank=True,
                                               null=True,
                                               verbose_name='Номер паспорта')
    passport_data_series = models.IntegerField(blank=True,
                                               null=True,
                                               verbose_name='Серия паспорта')
    place_of_passport_issuance = models.CharField(max_length=150,
                                                  verbose_name='Место выдачи паспорта',
                                                  blank=True,
                                                  null=True)
    date_of_issue = models.DateField(blank=True,
                                     null=True,
                                     verbose_name='Дата выдачи паспорта')
    # Адрес
    city = models.CharField(max_length=100,
                            blank=True,
                            null=True,
                            verbose_name='Город',
                            default='')
    street = models.CharField(max_length=100,
                              blank=True,
                              null=True,
                              verbose_name='Улица',
                              default='')
    home = models.CharField(max_length=10,
                            blank=True,
                            null=True,
                            verbose_name='Дом',
                            default='')
    flat = models.CharField(max_length=10,
                            blank=True,
                            default='',
                            verbose_name='Квартира')

    date_of_birth = models.DateField(blank=True,
                                     null=True,
                                     verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    phone_number = models.CharField(max_length=11,
                                    blank=True,
                                    null=True,
                                    verbose_name='Номер телефона',
                                    default='')

    def get_address(self):
        if self.flat != '':
            return 'Город {}, улица {}, дом {}, квартира {}'.format(self.city, self.street, self.home, self.flat)
        return 'Город {}, улица {}, дом {}'.format(self.city, self.street, self.home)

    def __str__(self):
        return self.user.username


class Applications(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    tag = models.CharField(max_length=100,
                           verbose_name='Краткое название проблемы',
                           default='')
    area_of_law = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name='Отрасль права',
                                   choices=[('Конституционное право', "Конституционное право"),
                                            ("Административное право", "Административное право"),
                                            ("Гражданское право", "Гражданское право"),
                                            ("Уголовное право", "Уголовное право"),
                                            ("Гражданское процессуальное право", "Гражданское процессуальное право"),
                                            ("Арбитражное процессуальное право", "Арбитражное процессуальное право"),
                                            ("Уголовно-процессуальное право", "Уголовно-процессуальное право"),
                                            ("Уголовно-исполнительное право", "Уголовно-исполнительное право"),
                                            ("Финансовое право", "Финансовое право"),
                                            ("Трудовое право", "Трудовое право"),
                                            ("Земельное право", "Земельное право")])
    application = models.TextField(verbose_name='Заявка', default='')
    status_of_application = models.CharField(max_length=100,
                                             default='Находится в обработке',
                                             verbose_name='Статус заявки',
                                             choices=[('Находится в обработке', "Находится в обработке"),
                                                      ("Идут торги", "Идут торги"),
                                                      ("Ожидание решения", "Ожидание решения"),
                                                      ("Заключен договор", "Заключен договор"),
                                                      ("Отказано в договоре", "Отказано в договоре"),
                                                      ("Заявка откланена", "Заявка откланена")])
    time_of_application_creature = models.DateTimeField(auto_now_add=True,
                                                        blank=True,
                                                        null=True,
                                                        verbose_name='Время создания заявки')
    time_of_application_accept = models.DateTimeField(blank=True,
                                                      null=True,
                                                      verbose_name='Время принятия заявки')
    time_of_application_placing = models.DateTimeField(blank=True,
                                                       null=True,
                                                       verbose_name='Время размещения заявки')
    time_of_first_response = models.DateTimeField(blank=True,
                                                  null=True,
                                                  verbose_name='Время первого ответа на заявку')


class LegalEntity(models.Model):
    is_legal_entity_profile = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name_of_the_organization = models.CharField(max_length=100,
                                                verbose_name='Наименование организации',
                                                null=True,
                                                default='Наименование организации')
    firstname_general_manager = models.CharField(max_length=100,
                                                 verbose_name='Имя генерального директора',
                                                 null=True,
                                                 default='Имя')
    lastname_general_manager = models.CharField(max_length=100,
                                                verbose_name='Фамилия генерального директора',
                                                null=True,
                                                default='Фамилия')
    patronymic_general_manager = models.CharField(max_length=100,
                                                  verbose_name='Отчество генерального директора',
                                                  null=True,
                                                  default='',
                                                  blank=True)
    main_state_registration_number = models.IntegerField(null=True,
                                                         blank=True,
                                                         verbose_name='Основной государственный регистрационный номер')
    organizational_and_legal_form = models.CharField(max_length=100,
                                                     blank=True,
                                                     null=True,
                                                     verbose_name='Организационно-правовая форма')
    taxpayer_identification_number = models.CharField(max_length=100,
                                                      blank=True,
                                                      null=True,
                                                      verbose_name='Идентификационный номер налогоплательщика')
    constituent_document = models.CharField(max_length=100,
                                            verbose_name='Учредительный документ',
                                            null=True,
                                            blank=True,
                                            choices=[('Устав', 'Устав'),
                                                     ('Типовой устав', 'Типовой устав'),
                                                     ('Учредительный договор', 'Учредительный договор')])
    code_of_the_reason_for_registration = models.IntegerField(null=True,
                                                              blank=True,
                                                              verbose_name='Код причины постановки на учет')
    Date_of_approval_of_the_constituent_document = models.DateField(blank=True,
                                                                    null=True,
                                                                    verbose_name='Дата утверждения учредительного договора')
    # Адрес
    legal_address = models.CharField(max_length=200,
                                     verbose_name='Юридический адрес',
                                     null=True,
                                     blank=True,)
    actual_address = models.CharField(max_length=200,
                                      verbose_name='Фактический адрес',
                                      null=True,
                                      blank=True,)

    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    phone_number = models.CharField(max_length=11,
                                    verbose_name='Номер телефона',
                                    default='')


class IndividualEntrepreneur(models.Model):
    is_individual_entrepreneur_profile = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
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

    main_state_registration_number_individual_entrepreneur = models.IntegerField(null=True,
                                                                                 blank=True,
                                                                                 verbose_name='Основной государственный регистрационный номер ИП')

    taxpayer_identification_number = models.CharField(max_length=100,
                                                      blank=True,
                                                      null=True,
                                                      verbose_name='Идентификационный номер налогоплательщика')
    number_of_the_registration_certificate = models.IntegerField(null=True,
                                                                 blank=True,
                                                                 verbose_name='Номер свидетельства о постановке на учет')
    Date_of_approval_of_the_registration_certificate = models.DateField(blank=True,
                                                                        null=True,
                                                                        verbose_name='Дата свидетельства о постановке на учет')
    # Адрес
    registration_address = models.CharField(max_length=200,
                                            verbose_name='Адрес регистрации',
                                            null=True,
                                            blank=True,)

    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    phone_number = models.CharField(max_length=11,
                                    verbose_name='Номер телефона',
                                    default='',
                                    blank=True)

