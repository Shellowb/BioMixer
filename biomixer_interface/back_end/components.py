from django_components import component


@component.register("calendar")
class Calendar(component.Component):
    def context(self, date):
        return {
            "date": date,
        }

    def template(self, context):
        return "[your app]/components/calendar/calendar.html"

    class Media:
        css = '[your app]/components/calendar/calendar.css'
        js = '[your app]/components/calendar/calendar.js'