from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               verbose_name='Автор',
                               related_name='author')
    contractor = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True,
                                   verbose_name='Исполнитель',
                                   related_name='contractor')
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
    application_text = models.TextField(verbose_name='Заявка', default='')
    status_of_application = models.CharField(max_length=100,
                                             default='Находится в обработке',
                                             verbose_name='Статус заявки',
                                             choices=[('Находится в обработке', "Находится в обработке"),
                                                      ("Идут торги", "Идут торги"),
                                                      ("Ожидание решения", "Ожидание решения"),
                                                      ("Заключен договор", "Заключен договор"),
                                                      ("Отказано в договоре", "Отказано в договоре"),
                                                      ("Заявка откланена", "Заявка откланена")])
    territory_of_the_host_application = models.CharField(max_length=100,
                                                         blank=True,
                                                         null=True,
                                                         verbose_name='Территория размещения заявки')
    current_application_price = models.CharField(max_length=10,
                                                 blank=True,
                                                 null=True,
                                                 verbose_name='Текущая цена заявки')
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

