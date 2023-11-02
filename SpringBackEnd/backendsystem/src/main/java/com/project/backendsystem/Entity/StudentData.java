package com.project.backendsystem.Entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class StudentData {
    @Id
    @GeneratedValue
    private long id;
    private String StudentName;
    private String City;
    private int RollNumber;
    private String Country;
}
