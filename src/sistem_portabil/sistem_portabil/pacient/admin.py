from django.contrib import admin
from django.contrib.auth.models import User
from .models import Pacient, DateMedicale, Recomandari, Adresa

admin.site.site_header = "Administrare Sistem Portabil"


class Adresadmin(admin.ModelAdmin):
    list_display = ('id', 'tara', 'judet', 'localitate', 'strada', 'user')
    search_fields = ('tara', 'judet', 'localitate')
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(Adresadmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

admin.site.register(Adresa, Adresadmin)


class PacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nume', 'prenume', 'user', 'user_pacient')
    list_display_links = ('id', 'nume', 'prenume')
    list_filter = ('nume', 'prenume')
    search_fields = ('nume', 'prenume')
    exclude = ['user', 'date_medicale', 'recomandari']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PacientAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['user_pacient'].queryset = User.objects.filter(groups__name='Pacient')
        context['adminform'].form.fields['adresa'].queryset = Adresa.objects.filter(user=request.user.id)
        return super(PacientAdmin, self).render_change_form(request, context, *args, **kwargs)

admin.site.register(Pacient, PacientAdmin)


class DateMedicaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'istoric_medical', 'alergii', 'consultatii_cardiologice', 'user')
    list_filter = ('istoric_medical', 'alergii', 'consultatii_cardiologice')
    search_fields = ('istoric_medical', 'alergii', 'consultatii_cardiologice')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(DateMedicaleAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs


admin.site.register(DateMedicale, DateMedicaleAdmin)


class RecomandariAdmin(admin.ModelAdmin):
    list_display = ('id', 'tip_recomandare', 'durata_zilnica', 'alte_indicatii', 'user')
    list_filter = ('tip_recomandare', 'durata_zilnica', 'alte_indicatii')
    search_fields = ('tip_recomandare', 'durata_zilnica', 'alte_indicatii')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(RecomandariAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs


admin.site.register(Recomandari, RecomandariAdmin)
