{
    'name': 'hospitalmanagement',
    'depends': ["base","website","stock"],
    'data': ['security/ir.model.access.csv',
             'views/patient.xml',
             'views/doctor.xml',
             'views/medication.xml',
             'views/appointment.xml',
             'views/appointment_booking.xml',
             'views/room.xml',
             'views/patient_in.xml',
             'views/patient_out.xml',
             'views/laboratry.xml',
             'views/doctor_department.xml',
             'views/product_stoc.xml',
             'wizard/prescription_wizard.xml',
             'menu/menu.xml'],
    'installable': True,
    'auto_install': False
}