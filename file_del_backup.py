#     # models.storage.new(self)
# else:
#     kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                              '%Y-%m-%dT%H:%M:%S.%f')
#     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                              '%Y-%m-%dT%H:%M:%S.%f')
#     del kwargs['__class__']
#     self.__dict__.update(kwargs)

# def __str__(self):
#     """Returns a string representation of the instance"""
#     cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#     return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)


# def all(self, cls=None):
#     # sec = {
#     #     'State': State,
#     #     'City': City,
#     #     # 'User': User,
#     #     # 'Amenity': Amenity,
#     #     # 'Place': Place,
#     #     # 'Review': Review
#     # }
#     if cls:
#         rows = self.__session.query(sec[cls]).all()
#         output = {}
#         for row in rows:
#             dict_ = {}
#             for col in row:
#                 dict_.update({f"{col.name}": f"{col}"})
#             key = "{}.{}".format(dict_['__class__'], dict_['id'])
#             output.update({key: dict_})
#         return output
#     else:
#         output = {}
#         for x in sec.keys():
#             output.update(self.all(x))
#             return output
