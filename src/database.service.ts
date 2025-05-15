import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class DatabaseService {
  constructor(private configService: ConfigService) {
    const dbUser = this.configService.get<string>('DB_USERNAME');
    const dbPassword = this.configService.get<string>('DB_PASSWORD');
    const dbHost = this.configService.get<string>('DB_HOST');
    const dbName = this.configService.get<string>('DB_NAME');
    const port = this.configService.get<string>('DB_PORT');
  }
}
