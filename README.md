<h1>InstagramDoodleMaker</h1>



This code creates doodles based on the image the user provides



Αυτός ο κώδικας δημιουργεί doodles με βαση τη φωτογραφία που δίνει ο χρήστης



Based on Python


> If you do not know who I am and happened to stumble upon this project, scroll to the bottom of this file for an English summary.

---

**<h2>INSTRUCTIONS:</h2>** 



Can only be used with phone link app (open the phone link app>open instagram>put the window as far left as possible let Windows maximize it )



Now on the Instagram app on the computer press the plus button click the color you want and just run the code 



<ins>If the code is running and you want to stop it the only thing you have to do is to get your mouse to the top left of the screen</ins>



Μπορεί να χρησιμοποιηθεί μόνο με την εφαρμογή Phone Link (ανοίξτε την εφαρμογή phone link > ανοίξτε το instagram > τοποθετήστε το παράθυρο τέρμα αριστερά και αφήστε τα Windows να το μεγιστοποιήσουν).



Τώρα, στην εφαρμογή του Instagram στον υπολογιστή, πατήστε το κουμπί συν (+), κάντε κλικ στο χρώμα που θέλετε και απλά τρέξτε τον κώδικα.



<ins>Αν ο κώδικας τρέχει και θέλετε να τον σταματήσετε, το μόνο που έχετε να κάνετε είναι να πάτε το ποντίκι σας τέρμα πάνω αριστερά στην οθόνη.</ins>



---



Γειά σου, για να είσαι εδώ, λογικά με ξέρεις αυτό είναι το μόνο από τα Project που έχω φτιάξει ως τώρα που σκέφτηκα να ανεβάσω στο github ,το έκανα έτσι για τη διαφορά, για να μπορώ να έχω ένα από τα επιτεύγματα μου και κάπου αλλού πέρα από τον σκληρό του υπολογιστή μου. Αυτό το project δεν είναι κάτι το ιδιαίτερο είναι ένας απλός κώδικας python.Mου είχε έρθει σαν ιδέα  όταν το instagram είχε κάνει το update με τα doodle.Η ικανότητα του υπολογιστή να ζωγραφίσει κάτι με τόσο μεγάλη ακρίβεια ειναι κάτι το συναρπαστικό για εμένα. Μου είχε αρέσει σαν ιδέα να βάζω το υπολογιστή μου να ζωγραφίζει εικόνες υψηλής ακριβείας καθώς τα doodles δεν επιτρέπουν την προώθηση φωτογραφιών για αυτό ότι έχει σταλεί σε μια συνομιλία σαν doodle θεωρείται και κάτι που είναι χειρόγραφο. Ευχαριστώ πολύ που είσαι εδώ και το διάβασες αυτό, κόβω την πολυλογία.







Πάμε στο κώδικα.

Αυτός ο κώδικας λειτουργεί με βάση δύο βιβλιοθήκες που μπορείς να δεις στην αρχή του κώδικα την cv2 και την pyautogui 

Για να συνοψίσω 

Η cv2 είναι βιβλιοθήκη για εικόνες έχει ικανότητες όπως επεξεργασία μετασχηματισμούς και ανίχνευση χρωματων.

Η pyautogui είναι βιβλιοθήκη που έχει την ικανότητα να ελέγχει το ποντίκι και το πληκτρολόγιο όπως θα έκανε ένας άνθρωπος αλλα με μαθηματική ακρίβεια 





Τώρα πολυ θα πουν << ε τελικά τι έκανες εσύ αφού σχεδόν όλα τα βασικά κομμάτια του κώδικα γίνονται από τις βιβλιοθήκες>>.Έχεις δίκιο,εγώ είπα στις βιβλιοθήκες πως και τι να κάνουν, που και πάλι ήθελε ένα ποσοστό σκέψης.



Αυτές οι δυο βιβλιοθήκες έχουν χρησιμοποιηθεί ώστε στην εικόνα που θα καταχωρηθεί αρχικά θα γίνει ασπρόμαυρη και έπειτα ο αλγόριθμος θα κοιτάξει κάθε pixel της εικόνας με αποτέλεσμα όπου βλέπει το μαύρο να πηγαίνει στο instagram και να κάνει ένα κλικ. Εδώ είναι η στιγμή που θα αναφέρω πως το πρόγραμμα είναι **αργό** (παρόλο που στο πρόγραμμα μικραίνω αρκετά την αρχική εικόνα ώστε να χωρέσει στην οθόνη του κινητού) το πρόγραμμα πρέπει να κοιτάξει πολλά(πρέπει να ελέγξει πολλά στοιχεία)ώστε να δημιουργηθεί το τελικό αποτέλεσμα, δεν μπορώ να απαντήσω ποσο χρόνο καθώς υπάρχουν διάφοροι παράγοντες που το επηρεάζουν. Παρόλο που η python δεν φημίζεται για την ταχύτητα της, εγώ ως προγραμματιστής φταίω για την διάρκεια καθώς αυτος ο αλγόριθμος ήταν ο πιο εύκολος ώστε να κανει την δουλειά που αναζητούσα.(συνήθως οι πιο απλοί αλγόριθμοι είναι και οι πιο αργοί **όχι πάντα**)

Ευχαριστώ πολύ αν διάβασες τα πάντα το εκτιμώ πραγματικά, αυτό για έμενα ήταν κάτι το διαφορετικό δεν ανεβάζω τη δουλειά μου online αλλά πιστευω ότι ολο και κάποιος μπορεί να το χρησιμοποιήσει.

---

This Python script automates the Instagram doodle feature by converting any image into a series of mouse clicks. Since Instagram treats doodles as manual drawings and doesn't allow direct image uploads, this tool uses OpenCV for image processing and PyAutoGUI to simulate a human hand. The algorithm scans the image pixel-by-pixel and "draws" it accurately on the screen. It is designed for precision rather than speed, providing a way to send high-detail images as authentic, hand-drawn doodles.
