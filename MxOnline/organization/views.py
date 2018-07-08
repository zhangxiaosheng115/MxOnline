# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from organization.models import CourseOrg, City


class OrgListView(View):

    def get(self, request):
        org_objects = CourseOrg.objects.all()
        hot_orgs = org_objects.order_by("-click_nums")[:3]  # 热门的机构

        city_objects = City.objects.all()

        city_id = request.GET.get("city", "")
        category = request.GET.get("ct", "")
        sort = request.GET.get("sort", "")

        if city_id:
            org_objects = org_objects.filter(city_id=int(city_id))

        if category:
            org_objects = org_objects.filter(category=category)

        if sort:
            if sort == "study_nums":
                org_objects = org_objects.order_by("-study_nums")
            if sort == "course_nums":
                org_objects = org_objects.order_by("-course_nums")

        try:
            page = request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1

        count = org_objects.count()

        p = Paginator(org_objects, 5, request=request)  # 对机构进行分页

        orgs = p.page(page)

        return render(request, 'org-list.html', {"org_objects": orgs,
                                                 "city_objects": city_objects,
                                                 "count": count,
                                                 "city_id": city_id,
                                                 "category": category,
                                                 "hot_orgs": hot_orgs,
                                                 "sort": sort
                                                 }
                      )

    def post(self, request):
        pass