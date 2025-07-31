import {
  Controller,
  Get,
  Post,
  Body,
  Param,
  Put,
  Delete,
  UseGuards,
} from '@nestjs/common';
import { PortfolioService } from './portfolio.service';
import { Portfolio } from './portfolio.entity';
import { CreatePortfolioDto } from './dto/create-portfolio.dto';
import { JwtAuthGuard } from '../auth/jwt-auth.guard';

@Controller('portfolios')
@UseGuards(JwtAuthGuard)
export class PortfolioController {
  constructor(private readonly portfolioService: PortfolioService) {}

  @Get()
  findAll(): Promise<Portfolio[]> {
    return this.portfolioService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string): Promise<Portfolio> {
    return this.portfolioService.findOne(+id);
  }

  @Post()
  create(@Body() createPortfolioDto: CreatePortfolioDto): Promise<Portfolio> {
    return this.portfolioService.create(createPortfolioDto);
  }

  @Put(':id')
  update(
    @Param('id') id: string,
    @Body() createPortfolioDto: CreatePortfolioDto,
  ): Promise<Portfolio> {
    return this.portfolioService.update(+id, createPortfolioDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string): Promise<void> {
    return this.portfolioService.remove(+id);
  }
}
