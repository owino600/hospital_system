#include "hospital.h"
/**
 * insert patient details
 */
int main()
{
	Patient* patientlist = NULL;
	int numPatient, patientID, contact;
	int i;
	char name[50], gender[50];

	printf("Enter Patient Number");
	scanf("%d", &numPatient);
	for (i = 0; i < numPatient; i++)
	{
		printf("ENTER PATIENT ID :");
		scanf("%d", &patientID);
		printf("PATIENT NAME :");
		scanf("%s", name);
		printf("PATIENT GENDER :");
		scanf("%s", gender);
		printf("CONTACTS :");
		scanf("%d", &contact);
		insertPatient(&patientlist, patientID, name, gender, contact);
	}
	/*display the list after inputs*/
	displayPatient(patientlist);
	return (0);
}
