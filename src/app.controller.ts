import { Body, Controller, Get, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { CreateUserOptionDto } from './dtos';

@Controller('api')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get('get-options')
  getOptions(): { body: string[] } {
    return { body: this.appService.getOptions() };
  }
  @Post('save')
  async save(@Body() data: CreateUserOptionDto): Promise<{ message: string }> {
    return await this.appService.save(data);
  }
}
