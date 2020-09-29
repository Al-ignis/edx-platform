
from django.core.management import call_command

from xmodule.modulestore.tests.django_utils import SharedModuleStoreTestCase


class BackfillOrgsAndOrgCoursesTest(SharedModuleStoreTestCase):
    """
    @@TODO
    """
    def test_placeholder(self):
        call_command("backfill_orgs_and_org_courses")
        assert True
