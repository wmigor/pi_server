import unittest

from pi_server import app, db, models, db_tools


class BaseDbTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
		app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
		app.config['TESTING'] = True
		db.app = app
		db.init_app(app)
		db.create_all()

	def setUp(self):
		db.session.rollback()
		self.transaction = db.session.begin(subtransactions=True)

	def tearDown(self):
		self.transaction.rollback()


class TestModels(BaseDbTest):

	def test_query(self):
		self.assertEqual([], models.User.query.all())
		self.assertEqual([], models.EquipmentType.query.all())
		self.assertEqual([], models.PortType.query.all())

	def test_fill_db(self):
		db_tools.fill_db()
		self.assertEqual(1, len(models.EquipmentType.query.all()))
		equip = models.EquipmentType.query.one()
		self.assertEqual(40, len(equip.equipment_port_types))


if __name__ == '__main__':
	unittest.main()
