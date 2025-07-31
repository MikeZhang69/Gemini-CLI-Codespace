import { IsString, IsObject, IsOptional } from 'class-validator';

export class CreatePortfolioDto {
  @IsString()
  name: string;

  @IsObject()
  @IsOptional()
  target_allocations: any;
}
