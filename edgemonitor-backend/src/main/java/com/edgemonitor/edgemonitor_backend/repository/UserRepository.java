package com.edgemonitor.edgemonitor_backend.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.edgemonitor.edgemonitor_backend.entity.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long>{
	
	Optional<User>  findFirstByEmail(String username);
}
