import { Injectable } from '@nestjs/common';
import { CreateUserOptionDto } from './dtos';
import { DataSource } from 'typeorm';

@Injectable()
export class AppService {
  constructor(private dataSource: DataSource) {}

  getHello(): string {
    return 'All Good';
  }
  async save(data: CreateUserOptionDto): Promise<{ message: string }> {
    const result = await this.dataSource.query(
      'INSERT INTO user_options (name, email, selected_option) VALUES (?,?,?)',
      [data.name, data.email, data.option],
    );
    return { message: 'User option saved successfully' };
  }
  getOptions(): string[] {
    return ['Agent', 'Main Corp', 'Accounting'];
  }
}
