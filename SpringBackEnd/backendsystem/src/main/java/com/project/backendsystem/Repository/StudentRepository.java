package com.project.backendsystem.Repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.project.backendsystem.Entity.StudentData;
@Repository
public interface StudentRepository extends JpaRepository<StudentData,Long> {

    List<StudentData> findByStudentName(String name);
    
}
