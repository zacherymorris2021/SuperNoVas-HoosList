#default choice values
PAYMENT_METHODS = (
    ('venmo', 'VENMO'),
    ('cash', 'CASH'),
    ('check', 'CHECK'),
    ('paypal', 'PAYPAL'),
    ('applePay', 'APPLEPAY'),
    ('none', 'NONE'),
    ('other', 'OTHER')
)
CONDITION_CHOICES = (
    ('new', 'NEW'),
    ('like new', 'LIKE NEW'),
    ('very good', 'VERY GOOD'),
    ('good', 'GOOD'),
    ('acceptable', 'ACCEPTABLE')
)
CATEGORIES = (
    ('furniture', 'FURNITURE'),
    ('textbooks', 'TEXTBOOKS'),
    ('clothing', 'CLOTHING'),
    ('class supplies', 'CLASS SUPPLIES'),
    ('kitchen', 'KITCHEN'),
    ('dorm', 'DORM'),
    ('uva gear', 'UVA GEAR'),
    ('electronics', 'ELECTRONICS'),
    ('other', 'OTHER')
)
RATING_CHOICES = (
    (0.0,'0-Awful'),
    (1.0,'1-Bad'),
    (2.0,'2-Poor'),
    (3.0,'3-Fair'),
    (4.0,'4-Good'),
    (5.0,'5-Great'),

)
