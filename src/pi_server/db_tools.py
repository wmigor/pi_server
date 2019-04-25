# coding: utf-8

from pi_server import models


def fill_db():
	gpio = models.PortType(name='GPIO')
	ground = models.PortType(name='Ground')
	power_3v = models.PortType(name='3.3v')
	power_5v = models.PortType(name='5v')
	reserved = models.PortType(name='Reserved')
	models.PortType.query.session.add_all([gpio, ground, power_3v, power_5v, reserved])
	raspberry = models.EquipmentType(name='Raspberry Pi 3')
	equipment_port_types = [
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=power_3v.id, number=1),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=power_5v.id, number=2),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=3),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=power_5v.id, number=4),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=5),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=6),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=7),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=8),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=9),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=10),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=11),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=12),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=13),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=14),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=15),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=16),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=power_3v.id, number=17),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=18),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=19),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=20),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=21),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=22),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=23),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=24),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=25),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=26),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=reserved.id, number=27),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=reserved.id, number=28),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=29),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=30),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=31),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=32),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=33),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=34),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=35),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=36),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=37),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=38),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=ground.id, number=39),
		models.EquipmentPortType(equipment_type_id=raspberry.id, port_type_id=gpio.id, number=40)
	]
	raspberry.equipment_port_types = equipment_port_types
	models.EquipmentType.query.session.add(raspberry)
