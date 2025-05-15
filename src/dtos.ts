import { IsEmail, IsNotEmpty, IsString } from 'class-validator';

export class CreateUserOptionDto {
  @IsNotEmpty()
  @IsString()
  name: string;

  @IsEmail()
  email: string;

  @IsNotEmpty()
  @IsString()
  option: string;
}
