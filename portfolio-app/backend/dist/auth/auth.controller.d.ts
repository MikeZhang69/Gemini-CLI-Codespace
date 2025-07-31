import { AuthService } from './auth.service';
import { SignupDto } from './dto/signup.dto';
import { LoginDto } from './dto/login.dto';
export declare class AuthController {
    private authService;
    constructor(authService: AuthService);
    signup(signupDto: SignupDto): Promise<import("../user/user.entity").User>;
    login(loginDto: LoginDto): Promise<{
        access_token: string;
    }>;
}
