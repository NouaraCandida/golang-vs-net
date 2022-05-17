//Student object
package models

type Student struct{
	ID int
	FirstName string 
	LastName string
	Age int
}

func NewStudent(firstName string, lastName string, age int) *Student{
	return&Student{
		FirstName : firstName,
		LastName : lastName,
		Age: age,
	}
}
