
records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
          ]


def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

class User:
	def __init__(self,user_id):
		self.user_id = user_id

	def __repr__(self):
		return 'User({})'.format(self.user_id)


users = [User(21), User(28), User(29)]
print(users)