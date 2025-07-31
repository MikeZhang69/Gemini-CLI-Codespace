import { Repository } from 'typeorm';
import { Portfolio } from './portfolio.entity';
export declare class PortfolioService {
    private portfoliosRepository;
    constructor(portfoliosRepository: Repository<Portfolio>);
    findAll(): Promise<Portfolio[]>;
    findOne(id: number): Promise<Portfolio>;
    create(portfolioData: Partial<Portfolio>): Promise<Portfolio>;
    update(id: number, portfolioData: Partial<Portfolio>): Promise<Portfolio>;
    remove(id: number): Promise<void>;
}
