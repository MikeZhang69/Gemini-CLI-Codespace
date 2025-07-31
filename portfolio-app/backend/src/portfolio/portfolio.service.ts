import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Portfolio } from './portfolio.entity';

@Injectable()
export class PortfolioService {
  constructor(
    @InjectRepository(Portfolio)
    private portfoliosRepository: Repository<Portfolio>,
  ) {}

  findAll(): Promise<Portfolio[]> {
    return this.portfoliosRepository.find();
  }

  findOne(id: number): Promise<Portfolio> {
    return this.portfoliosRepository.findOne({ where: { id } });
  }

  create(portfolioData: Partial<Portfolio>): Promise<Portfolio> {
    const portfolio = this.portfoliosRepository.create(portfolioData);
    return this.portfoliosRepository.save(portfolio);
  }

  async update(
    id: number,
    portfolioData: Partial<Portfolio>,
  ): Promise<Portfolio> {
    await this.portfoliosRepository.update(id, portfolioData);
    return this.findOne(id);
  }

  async remove(id: number): Promise<void> {
    await this.portfoliosRepository.delete(id);
  }
}
