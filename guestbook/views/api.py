import json

from django.http import HttpResponse
from django.views.generic import View

from guestbook.services.school import school_handler


def JSONResponse(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


class SchoolView(View):
    def get(self, request, *args, **kwargs):
        school_id = kwargs.pop('school_id', None)
        if school_id is None:
            return self.list()
        return self.retrieve(int(school_id))

    def retrieve(self, school_id):
        ret, status = self.response_exist(school_id)
        if not status:
            return ret

        return JSONResponse({'data':
            [
                {
                    'name': ret.name,
                    'numberOfClass': ret.number_of_class,
                    'id': ret.key.id()
                }
            ]
        })

    def list(self):
        all_school = school_handler.fetch_all_school()
        ret = []
        for school in all_school:
            ret.append({
                'name': school.name,
                'numberOfClass': school.number_of_class,
                'id': school.key.id()
            })
        return JSONResponse({'data': ret})

    def post(self, request, *args, **kwargs):
        name = request.DATA.get('name')
        number_of_class = request.DATA.get('numberOfClass')
        school = school_handler.create_school_obj(name, number_of_class)

        return JSONResponse({'data':
            [
                {
                    'name': school.name,
                    'numberOfClass': school.number_of_class,
                    'id': school.key.id()
                }
            ]
        })

    def delete(self, request, school_id, *args, **kwargs):
        ret, status = self.response_exist(school_id)
        if not status:
            return ret

        school_handler.delete_school_obj(ret)

        return JSONResponse({'data': 'Delete successfully'})

    @staticmethod
    def response_exist(school_id):
        school = school_handler.fetch_school_by_id(school_id)
        if school is None:
            return HttpResponse({'data': 'school id {} not found'.format(school_id)}), False
        return school, True

    def put(self, request, school_id, *args, **kwargs):
        ret, status = self.response_exist(school_id)
        if not status:
            return ret

        name = request.DATA.get('name')
        number_of_class = request.DATA.get('numberOfClass')

        ret = school_handler.update_school_obj(ret, name, number_of_class)

        return JSONResponse({'data':
            [
                {
                    'name': ret.name,
                    'numberOfClass': ret.number_of_class,
                    'id': ret.key.id()
                }
            ]
        })
