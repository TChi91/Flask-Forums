import copy, itertools


class BaseStore:

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def update(self, instance):
        result = instance
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == instance.id:
                all_members[index] = instance
                break

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)
        print "Member Deleted with success"

    def entity_exists(self, instance):
        result = True
        if self.get_by_id(instance.id) is None:
            result = False
        return result


class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        BaseStore.__init__(self, MemberStore.members, MemberStore.last_id)

    def get_by_name(self, name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == name:
                yield member

    def get_by_name2(self, name):
        all_members = self.get_all()
        return (member
                for member in all_members
                if member.name == name)

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())
        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)
        for member in all_members:
            yield member

    def get_top_two(self, posts_store):
        all_members = self.get_members_with_posts(posts_store)
        all_members = sorted(all_members, key=lambda member: member.posts, reverse=True)
        return all_members[:2]


class PostStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        BaseStore.__init__(self, PostStore.posts, PostStore.last_id)

    def get_by_title(self, title):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.title == title:
                result = title
                break
        return result

    def get_posts_by_date(self):
        all_posts = self.get_all()[:]
        all_posts.sort(key=lambda post: post.date, reverse=True)
        for post in all_posts:
            yield post
