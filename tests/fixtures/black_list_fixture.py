from datetime import datetime
from db.models import BlackList, db
from tests import fixtures


class BlackEmailFixture(object):
    def __init__(self) -> None:
        self.default_email = fixtures.RandomStringFixture()
        self.default_app_id = fixtures.RandomStringFixture()
        self.default_blocked_reason = fixtures.RandomStringFixture()
        self.default_created_ts = fixtures.ObjectFixture(datetime.now())
        self.default_ip_address = fixtures.RandomStringFixture()

    def create(self):
        email = self.default_email.create()
        app_id = self.default_app_id.create()
        blocked_reason = self.default_blocked_reason.create()
        created_ts = self.default_created_ts.create()
        ip_address = self.default_ip_address.create()

        instance = BlackList(email=email, app_id=app_id, blocked_reason=blocked_reason,
                             created_ts=created_ts, ip_address=ip_address)
        db.session.add(instance)
        db.session.commit()
        return instance
