from django.dispatch import Signal


obj_created = Signal(providing_args=["obj", "request"])
obj_updated = Signal(providing_args=["obj", "request"])
obj_deleted = Signal(providing_args=["obj", "request"])
