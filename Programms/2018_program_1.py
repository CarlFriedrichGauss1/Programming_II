'''
ΠΡΟΓΡΑΜΜΑ 1: Να γράψετε κλάση Vector3d για την κατασκευή διανυσµάτων στον χώρο. Η κλάση σας να
αποτελείται από τα πεδία x, y και z για τις συντεταγµένες. Τα πεδία δεν πρέπει να είναι ορατά εκτός της κλάσης
και η αρχικοποίηση τους ϑα γίνεται µε 3 πραγµατικούς αριθµούς. Η κλάση ϑα περιλαµβάνει τις εξής µεθόδους
αντικειµένου:
• Μέθοδο norm1 που να υπολογίζει τη νόρµα-1 (k~vk1 = |x| + |y| + |z|) ενός διανύσµατος.
• Μέθοδο cross_prod που να υπολογίζει το εξωτερικό γινόµενο δύο διανυσµάτων.Το εξωτερικό γινόµενο δύο
διανυσµάτων είναι επίσης διάνυσµα : (ax, ay, az) × (bx, by, bz) = (aybz − azby, azbx − axbz, axby − aybx).
• Μέθοδο µετατροπής διανύσµατος σε συµβολοσειρά.
Στη συνέχεια να γράψετε πρόγραµµα που να δηµιουργεί 2 διανύσµατα µε συντεταγµένες που δίνονται στην είσοδο,
να υπολογίζει και να εµφανίζει στην έξοδο (α) τη νόρµα τους, και (ϐ) το εξωτερικό γινόµενο.
ΠΡΟΓΡΑΜΜΑ 2: (α) Να γράψετε κλάση Product για τη δηµιουργία προϊόντων. Κάθε προϊόν έ
'''
import math

class Vector3d():
    def __init__(self,x,y,z):
        self.x  = x
        self.y = y
        self.z = z

    def norm1(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
        

    def cross_prod(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3d(cx, cy, cz)    
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v_1 = Vector3d(1,2,3)
v_2 = Vector3d(4,5,6)

norm1 = v_1.norm1()
norm2 = v_2.norm1()
cross_product = v_1.cross_prod(v_2)

print(norm1 , norm2 , cross_product)



