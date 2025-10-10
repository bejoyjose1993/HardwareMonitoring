package com.edgemonitor.edgemonitor_backend.services.auth;

import java.util.Optional;
import com.edgemonitor.edgemonitor_backend.dto.LoginRequest;
import com.edgemonitor.edgemonitor_backend.dto.SignupRequest;
import com.edgemonitor.edgemonitor_backend.dto.UserDto;
import com.edgemonitor.edgemonitor_backend.entity.User;

public interface AuthService {
	UserDto createUser(SignupRequest signupRequest);
	Optional<User> loginUser(LoginRequest loginRequest);
}
