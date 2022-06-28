from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation



class LevelPermission(models.Model):
    permission_title = models.CharField(max_length=40, blank=True, null=True)
    permission_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.permission_title

class UserDetails(models.Model):
    user_name = models.CharField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.user_name


class LevelMapping(models.Model):
    user_id = models.ManyToManyField(UserDetails)
    permissions = models.ManyToManyField(LevelPermission)

    def __str__(self):
        return self.level_name

class MainCompany(models.Model):
    company_name = models.CharField(max_length=240, blank=True,null=True)
    company_description = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.company_name

class CompanyDetails(models.Model):
    main_company = models.ForeignKey(MainCompany, on_delete=models.CASCADE)
    sub_company_name = models.CharField(max_length=240, blank=True, null=True, verbose_name="Company Name")
    sub_company_description = models.TextField(blank=True, null=True,verbose_name="Company Description")
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.sub_company_name

class PurchaseOrganisationDetails(models.Model):
    sub_company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    purchase_organisation_description = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.purchase_organisation_description

class LocationsDetails(models.Model):
    sub_company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    location_details = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.location_details

class ProductGroupDetails(models.Model):
    sub_company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    product_group_details = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.product_group_details

class PlantsDetails(models.Model):
    sub_company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    plants_details = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True,blank=True)
    content_object = GenericForeignKey()

    # parent = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True,related_name="children")

    # def get_children_filter(self,include_self=True):
    #     filters = Q(id=0)
    #     if include_self:
    #         filters |= Q(self.id)
    #     for i in PlantsDetails.objects.filter(parent=self):
    #         _a = i.get_children_filter(include_self=True)
    #         if _a:
    #             filters |= _a
    #     return filters
    
    # def get_all_children(self,include_self=True):
    #     table_name = PlantsDetails.objects.model.meta.db_table
    #     data_query = (
    #         "WITH RECURSIVE children (id) AS ("
    #         f" SELECT {table_name}.id FROM {table_name} WHERE id = {self.id}"
    #         " UNION ALL"
    #         f" SELECT {table_name}.id FROM children, {table_name}"
    #         f" WHERE {table_name}.parent_id = children.id"
    #         ")"
    #         f" SELECT {table_name}.id"
    #         f" FROM {table_name}, children WHERE children.id = {table_name}.id"
    #     )
    #     if not include_self:
    #         data_query += f" AND {table_name}.id != {self.id}"

    #     return PlantsDetails.objects.filter(id__in = [i.id for i in PlantsDetails.objects.raw(data_query)])



    def __str__(self):
        return self.plants_details

class StorageLocationDetails(models.Model):
    plants_details_data = GenericRelation(PlantsDetails)
    storage_location_details = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.storage_location_details

class CostCentersDetails(models.Model):
    plants_details_data = GenericRelation(PlantsDetails)
    cost_centers_details = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.cost_centers_details

class DepartmentsDetails(models.Model):
    plants_details_data = GenericRelation(PlantsDetails)
    departments_details = models.TextField(blank=True, null=True)
    level_mapping = models.ManyToManyField(LevelMapping)

    def __str__(self):
        return self.departments_details


