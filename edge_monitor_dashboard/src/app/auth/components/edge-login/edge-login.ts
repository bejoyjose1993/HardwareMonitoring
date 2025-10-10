import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth/auth.service';
import { StorageService } from '../../services/storage/storage.service';

@Component({
  selector: 'app-edge-login',
  standalone: false,
  templateUrl: './edge-login.html',
  styleUrl: './edge-login.scss'
})
export class EdgeLogin {
loginForm: FormGroup;
  error = '';

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private snackBar: MatSnackBar,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched(); // Show validation errors
      return;
    }

    const { email, password } = this.loginForm.value;

    this.authService.login({ email, password }).subscribe({
      next: (res) => {
        if (res.userId) {
          const user = { id: res.userId, role: 'Customer' };
          StorageService.saveUser(user);
          StorageService.saveToken(res.jwt);
          StorageService.login();

          this.snackBar.open('Login successful!', 'Close', {
            duration: 3000,
            panelClass: ['success-snackbar']
          });

          setTimeout(() => this.router.navigateByUrl('/dashboard'), 1000);
        } else {
          this.error = 'Invalid email or password.';
          this.snackBar.open(this.error, 'Close', {
            duration: 3000,
            panelClass: ['error-snackbar']
          });
        }
      },
      error: (err) => {
        if (err.status === 429) {
          this.error = 'Too many login attempts. Please try again later.';
        } else if (err.status === 401 || err.error?.message === 'Invalid credentials') {
          this.error = 'Invalid email or password.';
        } else {
          this.error = 'An unexpected error occurred.';
        }

        this.snackBar.open(this.error, 'Close', {
          duration: 3000,
          panelClass: ['error-snackbar']
        });
      }
    });
  }
}
