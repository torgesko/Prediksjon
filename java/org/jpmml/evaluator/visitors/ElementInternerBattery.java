/*
 * Copyright (c) 2018 Villu Ruusmann
 *
 * This file is part of JPMML-Evaluator
 *
 * JPMML-Evaluator is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * JPMML-Evaluator is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with JPMML-Evaluator.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.jpmml.evaluator.visitors;

import org.jpmml.model.visitors.MiningFieldInterner;
import org.jpmml.model.visitors.PredicateInterner;
import org.jpmml.model.visitors.ScoreDistributionInterner;
import org.jpmml.model.visitors.VisitorBattery;

public class ElementInternerBattery extends VisitorBattery {

	public ElementInternerBattery(){
		add(MiningFieldInterner.class);
		add(PredicateInterner.class);
		add(ScoreDistributionInterner.class);
	}
}