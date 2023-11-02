package com.project.backendsystem.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.project.backendsystem.Entity.StudentData;
import com.project.backendsystem.Repository.StudentRepository;

@RestController
public class APIConnect {
    
    @Autowired
    private StudentRepository repository;
    @PostMapping("/save")
    public String saveStudent(@RequestBody StudentData studentData)
    {
        repository.save(studentData);
        return "Student Data is Saved...";
    }
    @GetMapping("/getallstudent")
    public List<StudentData> getall()
    {
        return repository.findAll();
    }
    
    @GetMapping("/id/{name}")
    public List<StudentData> getStudentByName(@PathVariable String name)
    {
        return repository.findByStudentName(name);

    }
}
